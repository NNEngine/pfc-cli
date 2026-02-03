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
    mem_bytes = df.memory_usage(deep=True).sum()
    mem_mb = mem_bytes / (1024 * 1024)

    # ---------------- Summary ----------------
    summary = Table(
        title="Dataset Info",
        header_style="bold magenta"
    )

    summary.add_column("Property")
    summary.add_column("Value", justify="right")

    summary.add_row("File", session.file)
    summary.add_row("Rows", str(rows))
    summary.add_row("Columns", str(cols))
    summary.add_row("Memory Usage", f"{mem_mb:.2f} MB")

    console.print(summary)

    # ---------------- Column Info ----------------
    col_table = Table(
        title="Column Information",
        header_style="bold magenta"
    )

    col_table.add_column("Column")
    col_table.add_column("Dtype")
    col_table.add_column("Non-Null", justify="right")
    col_table.add_column("Nulls", justify="right")
    col_table.add_column("Null %", justify="right")

    for col in df.columns:
        total = len(df)
        non_null = df[col].count()
        nulls = total - non_null
        null_pct = (nulls / total) * 100 if total else 0

        col_table.add_row(
            col,
            str(df[col].dtype),
            str(non_null),
            str(nulls),
            f"{null_pct:.2f}%"
        )

    console.print(col_table)
