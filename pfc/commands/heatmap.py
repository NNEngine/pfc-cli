from pfc.core.state import session
from rich.console import Console
from rich.table import Table
import pandas as pd
import numpy as np

console = Console()

DEFAULT_BINS = 10
INTENSITY = " .:-=+*#%@"

def intensity_char(value, max_value):
    if max_value == 0:
        return " "
    idx = int((value / max_value) * (len(INTENSITY) - 1))
    return INTENSITY[idx]


def run(args):
    if session.df is None:
        console.print("[red]No dataset loaded[/red]")
        return

    if len(args) < 2:
        console.print(
            "[red]Usage:[/red] heatmap <x_column> <y_column> [value_column] [--bins N]"
        )
        return

    df = session.df.df.copy()

    x_col = args[0]
    y_col = args[1]
    value_col = None
    bins = DEFAULT_BINS

    if "--bins" in args:
        i = args.index("--bins")
        try:
            bins = int(args[i + 1])
        except Exception:
            console.print("[red]Bins must be an integer[/red]")
            return
        args = args[:i]

    if len(args) == 3:
        value_col = args[2]

    for col in [x_col, y_col]:
        if col not in df.columns:
            console.print(f"[red]Invalid column:[/red] {col}")
            return

    if value_col and value_col not in df.columns:
        console.print(f"[red]Invalid value column:[/red] {value_col}")
        return

    # ---- Bin numeric axes ----
    for col in [x_col, y_col]:
        if df[col].dtype.kind in "iufc":
            df[col] = pd.cut(df[col], bins=bins)

    # ---- Pivot ----
    if value_col:
        pivot = (
            df.pivot_table(
                index=y_col,
                columns=x_col,
                values=value_col,
                aggfunc="mean",
                observed=True
            )
        )
        title = f"Heatmap — mean({value_col})"
    else:
        pivot = (
            df.pivot_table(
                index=y_col,
                columns=x_col,
                values=df.columns[0],
                aggfunc="count",
                observed=True
            )
        )
        title = "Heatmap — density"

    pivot = pivot.fillna(0)

    max_value = pivot.values.max()

    # ---- Render ----
    table = Table(
        title=title,
        header_style="bold magenta",
        show_lines=False
    )

    table.add_column("Y \\ X")

    for col in pivot.columns:
        table.add_column(str(col)[:6], justify="center")

    for idx in pivot.index:
        row = [str(idx)[:6]]
        for col in pivot.columns:
            char = intensity_char(pivot.loc[idx, col], max_value)
            row.append(char)
        table.add_row(*row)

    console.print(table)
