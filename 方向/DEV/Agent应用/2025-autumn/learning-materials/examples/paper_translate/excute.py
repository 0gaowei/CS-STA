from pydantic_ai import Agent,RunContext
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIChatModel
import dotenv
import os
import requests
import re 
import json
import subprocess
import logfire
import asyncio
import time
from pydantic_ai.messages import ModelRequest, UserPromptPart,SystemPromptPart
from pydantic_ai.models import ModelRequestParameters
from pydantic import BaseModel
from tqdm.asyncio import tqdm_asyncio

dotenv.load_dotenv()

api_key = os.getenv('MODEL_API_KEY')
url = os.getenv("BASE_URL")
model_name = os.getenv("MODEL_NAME")
key = os.getenv('MINERU_API_KEY')
trans_model_name = os.getenv("TRANSALTE_MODEL_NAME")

# logfire.configure()
# logfire.instrument_pydantic_ai()

model = OpenAIChatModel(
    model_name = model_name,
    provider=OpenAIProvider(
        base_url=url,api_key=api_key,
    )
)

tran_model = OpenAIChatModel(
    model_name = model_name,
    provider=OpenAIProvider(
        base_url=url,api_key=api_key,
    )
)

class deps(BaseModel):
    key:str


class deps_file(deps):
    file_name:list

class deps_id(deps):
    batch_id:str

excute_prompt = """
# 角色
你是一名协调工具助手，能够自动将当前目录下的paper文件夹中所有论文翻译成中文，并可选导出为PDF。先获取文件，然后上传服务器转换md,然后调用命令下载，最后翻译。

# 技能
按照以下顺序调用工具
- check 检查是否已下载full.md,如果有，直接调用translate_md，没有则按照下面顺序进行;
- get_papername获得待翻译文件列表
- post将文件上传服务器
- get_status 获得处理文件
- translate_md将文件进行翻译

# 限制
你必须调用工具
""" 

translate_prompt = '''
# 角色
你是一名翻译大师，需要你将指定的md文件转化为中文。

# 限制
- 仅将md内的文字改成中文格式，不要动其他链接类的。
'''

excute_agent = Agent(
    model=model,
    system_prompt = excute_prompt,
    deps_type=deps,
)

@excute_agent.tool_plain
def check()->str:
    out = subprocess.run(['ls','result'],capture_output=True)
    file = out.stdout.decode()
    return file

@excute_agent.tool_plain
def get_papername() -> list:
    '获取待转换的pdf路径'
    par_path = subprocess.run(['pwd'],capture_output=True).stdout.decode().rstrip('\n')
    dir = subprocess.run(['ls','paper'],capture_output=True).stdout.decode().rstrip('\n').split('\n')
    return [par_path+'/paper/'+i for i  in dir]



@excute_agent.tool
def post(ctx:RunContext[deps],paths:list) -> str:
    paths = paths

    token = ctx.deps.key
    url = "https://mineru.net/api/v4/file-urls/batch"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = {
        "files": [
            {"name":"demo.pdf", "data_id": "abcd"}
        ],
        "model_version":"vlm",
        'language':'ch',
    }
    try:
        response = requests.post(url,headers=header,json=data)
        if response.status_code == 200:
            result = response.json()
            print('response success. result:{}'.format(result))
            if result["code"] == 0:
                batch_id = result["data"]["batch_id"]
                urls = result["data"]["file_urls"]
                print('batch_id:{},urls:{}'.format(batch_id, urls))
                for i in range(0, len(urls)):
                    with open(paths[i], 'rb') as f:
                        res_upload = requests.put(urls[i], data=f)
                        if res_upload.status_code == 200:
                            print(f"{urls[i]} upload success")
                        else:
                            print(f"{urls[i]} upload failed")
            else:
                print('apply upload url failed,reason:{}'.format(result.msg))
        else:
            print('response not success. status:{} ,result:{}'.format(response.status_code, response))
    except Exception as err:
        print(err)
        exit()
    return batch_id

@excute_agent.tool
def get_status(ctx:RunContext[deps],batch_id:str) -> str:
    url = f"https://mineru.net/api/v4/extract-results/batch/{batch_id}"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ctx.deps.key}"
    }
    res = requests.get(url, headers=header)
    while res.json()['data']['extract_result'][0]['state']!='done':
        res = requests.get(url, headers=header)
        time.sleep(1)
    return res.json()['data']['extract_result'][0]['full_zip_url']

@excute_agent.tool
def download_file(ctx:RunContext[deps],url:str) -> str:
    download = subprocess.run(['wget',url,'-O','result/file.zip'],capture_output=True)
    assert download.returncode == 0
    subprocess.run(['unzip','result/file.zip','-d','result/'])
    subprocess.run(['rm','result/file.zip'])
    return 'ok'


@excute_agent.tool_plain
async def translate_md():
    with open('result/full.md','r',encoding='utf-8') as f1:
        text = f1.read()
        paragraphs = [p.strip('\n') for p in text.split('\n\n') if p.strip('\n')]
    print(f"开始翻译 {len(paragraphs)} 个段落...")
    semaphore = asyncio.Semaphore(5)
    async def translate_with_limit(paragraph):
        async with semaphore:
            return await translate(paragraph)
    translated = await tqdm_asyncio.gather(
        *[translate_with_limit(p) for p in paragraphs],
        desc="翻译进度"
    )
    with open('result/translate.md','w+',encoding='utf-8') as f2:
        f2.write('\n\n'.join(translated))
    
    return 'ok'


async def translate(content:str) ->str:
    messages = [ModelRequest(parts=[SystemPromptPart(content='''将下列英文学术论文内容翻译成中文。要求：
1. 保持所有数学公式、代码、URL、邮箱地址不变
2. 参考文献不用翻译
3. 保持Markdown格式不变
4. 专业术语翻译准确
5. **不要添加额外解释**'''),UserPromptPart(content=content),])]
    model_settings = {}  
    model_request_parameters = ModelRequestParameters()  

    response = await tran_model.request(
        messages=messages,
        model_settings=model_settings,
        model_request_parameters=model_request_parameters
    )
    return response.text


run_result = asyncio.run(excute_agent.run(deps=deps(key=key)))
print(run_result.output)
