from pfc.core.state import session
from pfc.ui.table import render
from rich.console import Console

console = Console()


def run(args):
    if session.df is None:
        console.print("[red]No dataset loaded[/red]")
        return

    if not args:
        console.print("[red]Usage:[/red] select <col1> <col2> ...")
        return

    df = session.df.df  # pandas DataFrame
    available_cols = list(df.columns)

    # Handle column names with spaces (already split by shell)
    selected_cols = args

    # Validate columns
    invalid = [c for c in selected_cols if c not in available_cols]
    if invalid:
        console.print(
            f"[red]Invalid column(s):[/red] {', '.join(invalid)}"
        )
        console.print(
            f"[dim]Available columns:[/dim] {', '.join(available_cols)}"
        )
        return

    # Select columns (NON-MUTATING)
    result = df[selected_cols].copy()

    render(result, f"{session.file} (select: {', '.join(selected_cols)})")
