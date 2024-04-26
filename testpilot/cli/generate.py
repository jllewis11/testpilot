from ..agent.base import *
from ..utils.connector import select_service
from dotenv import load_dotenv
from openai import OpenAI
from langchain_together import Together
from pathlib import Path
import os

from rich.console import Console

console = Console()


def generator(service: str = "", path: Path = ""):
    """
    Generate code using the selected language model
    """
    load_dotenv()
    llm = select_service(service)
    console.print(f"Generating code using {llm}...")

    # TODO: Where to pull for the generated code?
    # Replace the example code below with the code you want to generate with
    if path != "" and path != "test":
        try:
            with open(path, "r") as f:
                code = f.read()
        except FileNotFoundError:
            raise Exception("File not found")

    elif path == "test":
        code = "def welcome():\n    return 'Hello, World!'"
    else:
        raise Exception("No path provided")

    if llm == "openai":
        openai_api_key = os.environ.get("OPENAI_API_KEY")
        console.print(openai_api_key)
        model = OpenAI(api_key=openai_api_key)
        agent = OpenAICodeGenerator(model)

        code = agent.generate_code(code)
        console.print(code)

        test_file = path.split(".py")[0]
        test_import = "from " + test_file.split("/")[-1] + " import * \n"
        test_file += "_test.py"

        code = test_import + code

        with open(test_file, "wb") as f:
            f.write(code.encode("ascii"))

    elif llm == "togetherai":
        key = os.getenv("TOGETHERAI_API_KEY")

        # List of LLMs available in TogetherAI
        # codellama/CodeLlama-7b-Python-hf
        # codellama/CodeLlama-13b-Python-hf

        model = Together(
            model="codellama/CodeLlama-7b-Python-hf",
            temperature=0.75,
            max_tokens=1024,
            top_k=1,
            repetition_penalty=1,
            together_api_key=key,
        )
        agent = TogetherCodeGenerator(model)

        code = agent.generate_code(code)
        console.print(code)
        test_file = path.split(".py")[0]
        test_import = "from " + test_file + " import * \n"
        test_file += "_test.py"

        with open(test_file, "wb") as f:
            f.write(code.encode("ascii"))
    else:
        raise Exception("Invalid service")
