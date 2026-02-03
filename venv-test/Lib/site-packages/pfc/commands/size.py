from pfc.core.state import session
from rich.console import Console
from rich.table import Table

console = Console()


def run(args):
    if session.df is None:
        console.print("[red]No dataset loaded[/red]")
        return

    df = session.df.df  # pandas DataFrame

    rows, cols = df.shape
    total = rows * cols

    table = Table(title="Dataset Size", header_style="bold magenta")

    table.add_column("Rows", justify="right")
    table.add_column("Columns", justify="right")
    table.add_column("Total Cells", justify="right")

    table.add_row(str(rows), str(cols), str(total))

    console.print(table)
