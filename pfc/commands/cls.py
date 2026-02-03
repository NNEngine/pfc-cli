import os
from rich.console import Console

console = Console()


def run(args):
    # Cross-platform clear
    os.system("cls" if os.name == "nt" else "clear")

    # Optional: reprint shell header
    console.print("[bold]pfc — Interactive Data Shell[/bold]")
    console.print(
        "Load a dataset once and explore it using built-in commands."
    )
    console.print(
        "Type 'help' to see available commands. Type 'exit' to quit.\n"
    )
