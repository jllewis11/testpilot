import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_openai import OpenAI
from langchain_together import Together
from rich.console import Console

console = Console()


def select_service(service: str = ""):
    """
    Set the API key for the specified service.
    """
    load_dotenv()
    dotenv_path = Path(".env")
    if not dotenv_path.exists():
        return None
    else:
        openai_api_key = os.getenv("OPENAI_API_KEY")
        togetherai_api_key = os.getenv("TOGETHERAI_API_KEY")
        if service == "openai":
            return OpenAI(openai_api_key)
        elif service == "togetherai":
            return Together(togetherai_api_key)
        else:
            if openai_api_key is not None:
                console.print("[bold green]Defaulting to OpenAI[/bold green]")
                return OpenAI(openai_api_key)
            elif togetherai_api_key is not None:
                console.print("[bold green]Defaulting to TogetherAI[/bold green]")
                return Together(togetherai_api_key)
            else:
                try:
                    raise Exception(
                        "No API key found. Please set an API key using the setkey command."
                    )
                except Exception:
                    console.print_exception()
