from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

model_client = OpenAIChatCompletionClient(
    model="qwen-max",
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "family": "unknown"
    },
    api_key=os.environ.get('DASHSCOPE_API_KEY'),
    base_url=os.environ.get('DASHSCOPE_API_BASE')
)