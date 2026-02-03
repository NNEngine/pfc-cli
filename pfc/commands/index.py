from pfc.core.state import session
from rich.console import Console
from rich.table import Table

console = Console()

PREVIEW_COUNT = 10


def run(args):
    if session.df is None:
        console.print("[red]No dataset loaded[/red]")
        return

    df = session.df.df  # pandas DataFrame
    index = df.index

    start_idx = index[0]
    end_idx = index[-1]
    total = len(index)

    # ---- Summary table ----
    summary = Table(
        title="Index Summary",
        header_style="bold magenta"
    )

    summary.add_column("Start Index", justify="right")
    summary.add_column("End Index", justify="right")
    summary.add_column("Total Rows", justify="right")

    summary.add_row(
        str(start_idx),
        str(end_idx),
        str(total)
    )

    console.print(summary)

    # ---- Preview table ----
    preview = Table(
        title=f"First {min(PREVIEW_COUNT, total)} Index Values",
        header_style="bold magenta"
    )

    preview.add_column("Position", justify="right")
    preview.add_column("Index Value", justify="right")

    for i, idx in enumerate(index[:PREVIEW_COUNT]):
        preview.add_row(str(i), str(idx))

    console.print(preview)
