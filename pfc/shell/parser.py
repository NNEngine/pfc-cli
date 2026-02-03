# pfc/shell/parser.py
from pfc.commands import head, tail, cols, load, help, describe, size, index, info, select, value_counts, groupby, unique, barplot, histplot, lineplot, cls, heatmap

COMMANDS = {
    "help": help.run,
    "cls": cls.run,

    "load": load.run,

    "head": head.run,
    "tail": tail.run,
    "cols": cols.run,

    "describe": describe.run,
    "size": size.run,

    "index": index.run,

    "info": info.run,

    "select": select.run,

    "value_counts": value_counts.run,

    "groupby": groupby.run,

    "unique": unique.run,

    #--------------------------------Visualization Commands-----------------------------------------

    "barplot": barplot.run,
    "histplot": histplot.run,
    "lineplot": lineplot.run,
    "heatmap": heatmap.run

}

def dispatch(cmd, args):
    if cmd in COMMANDS:
        COMMANDS[cmd](args)
    else:
        print("❌ Unknown command")
