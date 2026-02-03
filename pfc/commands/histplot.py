from pfc.core.state import session
from rich.console import Console
from rich.table import Table
import numpy as np

console = Console()

DEFAULT_BINS = 10
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
        console.print("[red]Usage:[/red] hist <numeric_column> [bins]")
        return

    df = session.df.df
    col = args[0]

    # ---- Validate column ----
    if col not in df.columns:
        console.print(f"[red]Invalid column:[/red] {col}")
        return

    if not df[col].dtype.kind in "iufc":
        console.print(
            f"[yellow]Column '{col}' is not numeric[/yellow]"
        )
        console.print("[dim]Tip:[/dim] Use barplot / value_counts for categorical data.")
        return

    # ---- Bins ----
    bins = DEFAULT_BINS
    if len(args) > 1:
        try:
            bins = int(args[1])
            if bins <= 0:
                raise ValueError
        except ValueError:
            console.print("[red]Bins must be a positive integer[/red]")
            return

    data = df[col].dropna().values

    if len(data) == 0:
        console.print("[yellow]No data available for histogram[/yellow]")
        return

    # ---- Compute histogram ----
    counts, edges = np.histogram(data, bins=bins)
    max_count = counts.max()

    # ---- Build table ----
    table = Table(
        title=f"Histogram — {col} ({bins} bins)",
        header_style="bold magenta"
    )

    table.add_column("Range")
    table.add_column("Count", justify="right")
    table.add_column("Bar")

    for i in range(len(counts)):
        left = edges[i]
        right = edges[i + 1]
        label = f"{left:.2f} – {right:.2f}"

        table.add_row(
            label,
            str(counts[i]),
            make_bar(counts[i], max_count)
        )

    console.print(table)
