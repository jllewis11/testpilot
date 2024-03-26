from ..agent.base import *
from ..utils.connector import select_service
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_together import Together
from pathlib import Path
import os

from rich.console import Console

console = Console()

def generator(service: str = ""):
    load_dotenv()
    llm = select_service(service)

    if llm == "openai":
        key = os.getenv("OPENAI_API_KEY")
        model = OpenAI(openai_api_key=key)
        agent = OpenAICodeGenerator(model)

        #TODO: Where to pull for the generated code?
        
        code = agent.generate_code("def welcome():\n    return 'Hello, World!'")
        console.print(code)
    elif llm == "togetherai":
        key = os.getenv("TOGETHERAI_API_KEY")
        model = Together(togetherai_api_key=key)
        agent = TogetherCodeGenerator(model)

        code = agent.generate_code("def welcome():\n    return 'Hello, World!'")
        console.print(code)
    else:
        raise Exception("Invalid service")
        

