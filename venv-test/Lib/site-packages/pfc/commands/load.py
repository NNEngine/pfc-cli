from pfc.core.state import session
from pfc.core.dataset import Dataset
from rich.console import Console

console = Console()


def run(args):
    if not args:
        console.print("[red]Usage:[/red] load <file.csv>")
        return

    path = args[0]

    try:
        dataset = Dataset(path)
    except Exception as e:
        console.print(f"[red]Failed to load CSV:[/red] {e}")
        return

    session.df = dataset
    session.file = path

    console.print(f"[bold green]Loaded[/bold green] {path}")
