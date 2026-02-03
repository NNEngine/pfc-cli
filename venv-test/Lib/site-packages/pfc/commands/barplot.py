from pfc.core.state import session
from rich.console import Console
from rich.table import Table

console = Console()

MAX_UNIQUE = 20
BAR_WIDTH = 25
BAR_CHAR = "█"
EMPTY_CHAR = "░"


def make_bar(value, max_value, width=BAR_WIDTH):
    if max_value == 0:
        return ""
    filled = int((value / max_value) * width)
    return BAR_CHAR * filled + EMPTY_CHAR * (width - filled)


def run(args):
    if session.df is None:
        console.print("[red]No dataset loaded[/red]")
        return

    if not args:
        console.print("[red]Usage:[/red] barplot <column>")
        return

    df = session.df.df
    col = " ".join(args)

    if col not in df.columns:
        console.print(f"[red]Invalid column:[/red] {col}")
        return

    counts = df[col].value_counts(dropna=False)

    if len(counts) > MAX_UNIQUE:
        console.print(
            f"[yellow]Cannot plot column '{col}':[/yellow] "
            f"{len(counts)} unique values (limit is {MAX_UNIQUE})"
        )
        console.print("[dim]Tip:[/dim] Use `value_counts` instead.")
        return

    max_value = counts.max()

    table = Table(
        title=f"Bar Plot — {col}",
        header_style="bold magenta"
    )

    table.add_column("Value")
    table.add_column("Count", justify="right")
    table.add_column("Bar", justify="left")

    for value, count in counts.items():
        table.add_row(
            str(value),
            str(count),
            make_bar(count, max_value)
        )

    console.print(table)
