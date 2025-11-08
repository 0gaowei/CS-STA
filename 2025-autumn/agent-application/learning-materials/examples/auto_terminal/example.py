from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from dotenv import load_dotenv
import os
from pydantic_ai import Agent
import logfire
import sys
import readline
from datetime import datetime
import subprocess
import asyncio

load_dotenv() 
api_key = os.getenv('SILICONFLOW_API_KEY')

# logfire.configure()
# logfire.instrument_pydantic_ai()

llm = OpenAIChatModel(
    'Qwen/Qwen3-30B-A3B-Instruct-2507',
    provider = OpenAIProvider(
        base_url = 'https://api.siliconflow.cn/v1',
        api_key=api_key,
    )
)
prompt='''
### 角色：
你是一名智能助手，能够出色完成用户所给任务。

### 技能
1、你可以尽情调用一切所提供的工具
2、自我解决错误直到任务完成

### 限制
当出现错误时，尽量反思，然后自我解决
'''


agent = Agent(
    llm,
    system_prompt=prompt,
)



@agent.tool_plain
def get_now_time() ->datetime:
    """get the current time

    Returns:
        datetime: The time
    """    
    return datetime.now()

@agent.tool_plain
def read_file_content(path:str):
    """Use this tool to read the file content

    Args:
        path (str): file path

    Returns:
        _type_: content
    """    
    try :
        with open(path,'r',encoding='utf-8') as f:
            text=f.readlines()
    except FileExistsError as e:
        return f"ERROR:{e}"

@agent.tool_plain
def create_file(path:str,content:str):
    """create one file you wanted

    Args:
        path (str): the file path
        content (str): the content you want to write
    """    
    try:
        with open(path,'w+',encoding='utf-8') as f:
            f.write(content)
        return 'The file has been created!'
    except Exception as e:
        return f'ERROR:{e}'

@agent.tool_plain
def execute_sys_cmd(cmd:str):
    """This tool allow you execute the system command

    Args:
        cmd (str): The command
    """    
    user_cof=input(f"将要执行命令{cmd},是否执行(y/n)")
    if user_cof.lower() == 'y':
        try:
            result=subprocess.run(
                cmd,
                shell=True,
                text=True,
                capture_output=True,
                check=True,
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f'ERROR:{e}'
        except FileExistsError as e:
            return f'ERROR:{e}'
    elif user_cof.lower() == 'n':
        return "用户拒绝了命令"
    else:
        print("请重新输入")
        result = execute_sys_cmd(cmd)
        return result

async def main():
    user_in = input('用户:\n')
    new_msg = ''
    while user_in.lower() not in ['q','exit']:
        res = await agent.run(user_in,message_history=new_msg,)
        print('AI:\n'+res.output+'\n')  
        new_msg = res.new_messages()  
        user_in = input('用户:\n')

asyncio.run(main())