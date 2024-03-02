import typer
from rich.console import Console
from testpilot.key import setkey, viewkey, removekey

console = Console()
app = typer.Typer()

app.command()(setkey)
app.command()(viewkey)
app.command()(removekey)

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")

