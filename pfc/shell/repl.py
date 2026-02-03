# pfc/shell/repl.py
from pfc.shell.parser import dispatch

def start():
    print("pfc — Interactive Data Shell")
    print("Load a dataset once and explore it using built-in commands.")
    print("Type 'help' to see available commands. Type 'exit' to quit.\n")

    while True:
        raw = input("pfc> ").strip()
        if not raw:
            continue

        if raw in {"exit", "quit"}:
            break

        parts = raw.split()
        dispatch(parts[0], parts[1:])
