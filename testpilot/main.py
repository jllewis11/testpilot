import typer
from rich.console import Console
from testpilot.cli.key import setkey, viewkey, removekey
from testpilot.cli.generate import generator


console = Console()
app = typer.Typer()


@app.command()
def set_key():
    setkey()


@app.command()
def view_key():
    viewkey()


@app.command()
def remove_key():
    removekey()


@app.command()
def generate(service: str = "", path: str = ""):
    generator(service, path)


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def version():
    typer.echo("0.1.0")
