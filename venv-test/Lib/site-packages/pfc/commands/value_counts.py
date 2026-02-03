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
        console.print("[red]Usage:[/red] value_counts <column> [--normalize]")
        return

    df = session.df.df
    normalize = False

    if "--normalize" in args:
        normalize = True
        args.remove("--normalize")

    col = " ".join(args)

    if col not in df.columns:
        console.print(f"[red]Invalid column:[/red] {col}")
        return

    counts = df[col].value_counts(dropna=False)

    result = pd.DataFrame({
        col: counts.index.astype(str),
        "Count": counts.values
    })

    if normalize:
        total = result["Count"].sum()
        result["Percentage"] = (result["Count"] / total * 100).round(2)

    render(result, f"{session.file} (value_counts: {col})")
