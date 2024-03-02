import typer
from dotenv import load_dotenv, set_key
from pathlib import Path
import os



def setkey(service: str,api_key: str):
    """
    Set the API key for the specified service.
    """
    dotenv_path = Path('.env')
    if not dotenv_path.exists():
        dotenv_path.touch()

    if service == "openai":
        set_key(dotenv_path.resolve(), "OPENAI_API_KEY", api_key)
        typer.echo("OpenAI API key stored successfully.")
    elif service == "togetherai":
        set_key(dotenv_path.resolve(), "TOGETHERAI_API_KEY", api_key)
        typer.echo("TogetherAI API key stored successfully.")
    else:
        typer.echo("Invalid service. Please choose 'openai' or 'togetherai'.")

def viewkey():
    """
    View the current API keys for OpenAI and TogetherAI.
    """
    # Ensure environment variables are loaded
    load_dotenv()

    # Retrieve API keys
    openai_api_key = os.getenv("OPENAI_API_KEY")
    togetherai_api_key = os.getenv("TOGETHERAI_API_KEY")

    # Check and display OpenAI API key
    if openai_api_key:
        masked_openai_key = f"{openai_api_key[:-4].replace(openai_api_key[:-4], '*' * len(openai_api_key[:-4]))}{openai_api_key[-4:]}"
        typer.echo(f"Current OpenAI API Key: {masked_openai_key}")
    else:
        typer.echo("No OpenAI API key is set.")

    # Check and display TogetherAI API key
    if togetherai_api_key:
        masked_togetherai_key = f"{togetherai_api_key[:-4].replace(togetherai_api_key[:-4], '*' * len(togetherai_api_key[:-4]))}{togetherai_api_key[-4:]}"
        typer.echo(f"Current TogetherAI API Key: {masked_togetherai_key}")
    else:
        typer.echo("No TogetherAI API key is set.")

def removekey(service: str):
    """
    Remove the current API key for the specified service.
    """
    dotenv_path = Path('.env')
    key_name = ""

    if service == "openai":
        key_name = "OpenAI API Key"
    elif service == "togetherai":
        key_name = "TogetherAI API Key"
    else:
        typer.echo("Invalid service. Please choose 'openai' or 'togetherai'.")
        return

    if typer.confirm(f"Are you sure you want to remove the {key_name}?"):
        set_key(dotenv_path.resolve(), f"{service.upper()}_API_KEY", "")
        typer.echo(f"{key_name} removed successfully.")
    else:
        typer.echo("Operation cancelled.")