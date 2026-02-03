from pfc.core.state import session
from rich.console import Console
from rich.table import Table

console = Console()


def run(args):
    if session.df is None:
        console.print("[red]No dataset loaded[/red]")
        return

    table = Table(title="Columns", header_style="bold magenta")

    table.add_column("Index", justify="right")
    table.add_column("Name")

    for i, col in enumerate(session.df.columns()):
        table.add_row(str(i), col)

    console.print(table)
