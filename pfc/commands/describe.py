from pfc.core.state import session
from rich.console import Console
from rich.table import Table

console = Console()


def run(args):
    if session.df is None:
        console.print("[red]No dataset loaded[/red]")
        return

    df = session.df.df

    # ---- Select columns ----
    if args:
        cols = []
        non_numeric = []

        for col in args:
            if col not in df.columns:
                console.print(f"[red]Invalid column:[/red] {col}")
                return

            if not df[col].dtype.kind in "iufc":  # int, unsigned, float, complex
                non_numeric.append(col)
            else:
                cols.append(col)

        if non_numeric:
            console.print(
                "[yellow]Cannot describe non-numeric column(s):[/yellow] "
                + ", ".join(non_numeric)
            )
            console.print(
                "[dim]Tip:[/dim] Use `value_counts` or `unique` for categorical columns."
            )
            return

        data = df[cols]

    else:
        data = df.select_dtypes(include="number")

    if data.empty:
        console.print("[yellow]No numeric columns available to describe[/yellow]")
        return

    desc = data.describe()

    # ---- Render table ----
    table = Table(
        title="Dataset Description",
        header_style="bold magenta",
        row_styles=["none", "dim"]
    )

    table.add_column("Metric")

    for col in desc.columns:
        table.add_column(col, justify="right")

    for idx in desc.index:
        table.add_row(
            idx,
            *[f"{desc[col][idx]:.3f}" for col in desc.columns]
        )

    console.print(table)
