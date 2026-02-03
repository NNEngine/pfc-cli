# # pfc/ui/table.py
# from rich.table import Table
# from rich.console import Console

# console = Console()

# def render(df, title):
#     table = Table(title=title, header_style="bold magenta", row_styles=["none", "dim"])
#     for col in df.columns:
#         table.add_column(col, max_width=20, overflow="ellipsis")

#     for _, row in df.iterrows():
#         table.add_row(*[str(v) for v in row])

#     console.print(table)

# from rich.console import Console
# from rich.table import Table

# console = Console()

# MAX_VISIBLE_ROWS = 10


# def render(df, title):
#     table = Table(
#         title=title,
#         header_style="bold magenta",
#         row_styles=["none", "dim"]
#     )

#     for col in df.columns:
#         table.add_column(col, max_width=20, overflow="ellipsis")

#     for _, row in df.iterrows():
#         table.add_row(*[str(v) for v in row])

#     # 🔥 Scroll if too many rows
#     if len(df) > MAX_VISIBLE_ROWS:
#         with console.pager():
#             console.print(table)
#     else:
#         console.print(table)

from rich.console import Console
from rich.table import Table
import os

console = Console()
MAX_VISIBLE_ROWS = 10


def render(df, title):
    rows = len(df)

    # 🔵 Case 1: Small table → normal render
    if rows <= MAX_VISIBLE_ROWS:
        _print_table(df, title)
        return

    # 🔵 Case 2: Unix → pager
    if os.name != "nt":
        with console.pager():
            _print_table(df, title)
        return

    # 🔵 Case 3: Windows → manual paging
    _render_windows_paged(df, title)


def _print_table(df, title):
    table = Table(
        title=title,
        header_style="bold magenta",
        row_styles=["none", "dim"],
        show_lines=False
    )

    for col in df.columns:
        table.add_column(col, max_width=20, overflow="ellipsis")

    for _, row in df.iterrows():
        table.add_row(*[str(v) for v in row])

    console.print(table)


def _render_windows_paged(df, title):
    total = len(df)
    start = 0

    while start < total:
        end = min(start + MAX_VISIBLE_ROWS, total)
        chunk = df.iloc[start:end]

        page_title = f"{title}  (rows {start + 1}-{end})"
        _print_table(chunk, page_title)

        start = end
        if start >= total:
            break

        console.print("[dim]Press Enter for next page, q to quit[/dim]", end="")
        choice = input().strip().lower()
        if choice == "q":
            break
