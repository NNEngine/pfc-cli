from pfc.core.state import session
from pfc.ui.table import render
from rich.console import Console
import pandas as pd

console = Console()


def run(args):
    if session.df is None:
        console.print("[red]No dataset loaded[/red]")
        return

    if not args:
        console.print("[red]Usage:[/red] unique <column> [--count]")
        return

    df = session.df.df

    show_count = False
    if "--count" in args:
        show_count = True
        args.remove("--count")

    col = " ".join(args)

    if col not in df.columns:
        console.print(f"[red]Invalid column:[/red] {col}")
        console.print(f"[dim]Available columns:[/dim] {', '.join(df.columns)}")
        return

    if show_count:
        vc = df[col].value_counts(dropna=False)
        result = pd.DataFrame({
            col: vc.index.astype(str),
            "Count": vc.values
        })
        title = f"{session.file} (unique counts: {col})"
    else:
        uniques = df[col].drop_duplicates()
        result = pd.DataFrame({col: uniques.astype(str).values})
        title = f"{session.file} (unique: {col})"

    render(result, title)
