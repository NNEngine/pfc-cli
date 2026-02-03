from pfc.core.state import session
from rich.console import Console
from rich.table import Table
import pandas as pd

console = Console()

MAX_RENDER_POINTS = 50
HEIGHT = 10
POINT_CHAR = "●"
EMPTY_CHAR = " "


def run(args):
    if session.df is None:
        console.print("[red]No dataset loaded[/red]")
        return

    if len(args) < 2:
        console.print("[red]Usage:[/red] lineplot <x_column> <y_column> [--agg mean|sum|min|max|count]")
        return

    df = session.df.df

    x_col = args[0]
    y_col = args[1]

    agg = "mean"
    if "--agg" in args:
        idx = args.index("--agg")
        try:
            agg = args[idx + 1]
        except IndexError:
            console.print("[red]Missing aggregation after --agg[/red]")
            return

    if x_col not in df.columns:
        console.print(f"[red]Invalid x column:[/red] {x_col}")
        return

    if y_col not in df.columns:
        console.print(f"[red]Invalid y column:[/red] {y_col}")
        return

    if not df[y_col].dtype.kind in "iufc":
        console.print(f"[red]Y column must be numeric:[/red] {y_col}")
        return

    if agg not in {"mean", "sum", "min", "max", "count"}:
        console.print("[red]Invalid aggregation[/red]")
        return

    # ---- Aggregate ----
    grouped = (
        df.groupby(x_col)[y_col]
        .agg(agg)
        .reset_index()
        .sort_values(x_col)
    )

    n_points = len(grouped)
    step = 1

    if n_points > MAX_RENDER_POINTS:
        step = (n_points + MAX_RENDER_POINTS - 1) // MAX_RENDER_POINTS
        grouped = grouped.iloc[::step].reset_index(drop=True)

        console.print(
            f"[dim]Downsampling applied:[/dim] showing every {step} point "
            f"({len(grouped)} of {n_points})"
        )


    y_values = grouped[y_col].values
    y_min, y_max = y_values.min(), y_values.max()

    # Normalize Y to HEIGHT
    def scale(y):
        if y_max == y_min:
            return HEIGHT // 2
        return int((y - y_min) / (y_max - y_min) * (HEIGHT - 1))

    scaled = [scale(y) for y in y_values]

    # ---- Build plot grid ----
    grid = [[EMPTY_CHAR] * len(scaled) for _ in range(HEIGHT)]

    for x, y in enumerate(scaled):
        grid[HEIGHT - 1 - y][x] = POINT_CHAR

    # ---- Render ----
    table = Table(
        title=f"Line Plot — {y_col} vs {x_col} ({agg})",
        header_style="bold magenta"
    )

    table.add_column("Y")
    table.add_column("Plot")

    for i, row in enumerate(grid):
        y_label = f"{y_max - i * (y_max - y_min) / (HEIGHT - 1):.2f}"
        table.add_row(y_label, "".join(row))

    table.add_row("", "-" * len(scaled))
    table.add_row("X", " ".join(str(x)[:1] for x in grouped[x_col]))

    console.print(table)
    console.print(
        "[dim]Note:[/dim] X-axis is sampled; gaps reflect uneven data distribution."
    )
