# pfc/commands/head.py
from pfc.core.state import session
from pfc.ui.table import render

def run(args):
    if session.df is None:
        print("❌ No dataset loaded")
        return

    n = int(args[0]) if args else 5
    render(session.df.head(n), f"{session.file} (head {n})")
