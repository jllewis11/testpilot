import typer
from rich.console import Console
from testpilot.cli.key import setkey, viewkey, removekey
from testpilot.cli.generate import generateOpenAI, generateTogetherAI

console = Console()
app = typer.Typer()

app.command()(setkey)
app.command()(viewkey)
app.command()(removekey)
# app.commmand()(generateOpenAI)
# app.command()(generateTogetherAI)


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def version():
    typer.echo("0.1.0")
