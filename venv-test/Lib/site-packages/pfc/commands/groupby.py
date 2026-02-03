from pfc.core.state import session
from pfc.ui.table import render
from rich.console import Console

console = Console()

ALLOWED_AGGS = {"count", "mean", "sum", "min", "max"}


def run(args):
    if session.df is None:
        console.print("[red]No dataset loaded[/red]")
        return

    if len(args) < 3:
        console.print(
            "[red]Usage:[/red] groupby <group_col...> <agg_column> <agg_func>"
        )
        console.print(
            f"[dim]Allowed agg_func:[/dim] {', '.join(ALLOWED_AGGS)}"
        )
        return

    df = session.df.df

    agg_func = args[-1]
    agg_col = args[-2]
    group_cols = args[:-2]

    # ---- Validate agg func ----
    if agg_func not in ALLOWED_AGGS:
        console.print(f"[red]Invalid aggregation function:[/red] {agg_func}")
        return

    # ---- Validate columns ----
    for col in group_cols + [agg_col]:
        if col not in df.columns:
            console.print(f"[red]Invalid column:[/red] {col}")
            return

    # ---- Perform groupby ----
    result = (
        df
        .groupby(group_cols)[agg_col]
        .agg(agg_func)
        .reset_index()
    )

    # ---- Rename aggregated column ----
    result.rename(
        columns={agg_col: f"{agg_func.upper()}({agg_col})"},
        inplace=True
    )

    render(
        result,
        f"{session.file} (groupby {', '.join(group_cols)} → {agg_func} {agg_col})"
    )
