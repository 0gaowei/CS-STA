from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from dotenv import load_dotenv
import os
from pydantic_ai import Agent


load_dotenv() 
api_key = os.getenv('SILICONFLOW_API_KEY')


llm = OpenAIChatModel(
    'Qwen/Qwen3-30B-A3B-Instruct-2507',
    provider = OpenAIProvider(
        base_url = 'https://api.siliconflow.cn/v1',
        api_key=api_key,
    )
)

prompt='''
### 角色：
你是一名智能助手，能够出色完成用户所给任务

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


rst1 = agent.run_sync('你好，我是松')
print(rst1)

rst2 = agent.run_sync('我叫什么')
print(rst2)