from rich.console import Console
from rich.table import Table

console = Console()


def section(table, title):
    table.add_row(
        f"[bold magenta]{title}[/bold magenta]",
        ""
    )


def run(args):
    table = Table(
        title="pfc — Command Reference",
        header_style="bold magenta",
        show_lines=False
    )

    table.add_column("Command", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")

    # ── Session & Shell ──────────────────────────────
    section(table, "Session & Shell")
    table.add_row("help", "Show this help summary")
    table.add_row("cls", "Clear the terminal screen (keeps dataset loaded)")
    table.add_row("exit", "Exit the interactive shell")

    table.add_row("", "")  # spacer

    # ── Data Loading ─────────────────────────────────
    section(table, "Data Loading")
    table.add_row("load <file.csv>", "Load a CSV file into the current session")

    table.add_row("", "")

    # ── Data Structure & Metadata ────────────────────
    section(table, "Data Structure & Metadata")
    table.add_row("cols", "List all column names")
    table.add_row("index", "Show dataset index range and preview")
    table.add_row("size", "Show dataset dimensions (rows × columns)")
    table.add_row("info", "Show dataset metadata and column information")

    table.add_row("", "")

    # ── Data Viewing ─────────────────────────────────
    section(table, "Data Viewing")
    table.add_row("head [n]", "Display the first n rows of the dataset (default: 5)")
    table.add_row("tail [n]", "Display the last n rows of the dataset (default: 5)")

    table.add_row("", "")

    # ── Column Operations ────────────────────────────
    section(table, "Column Operations")
    table.add_row("select <col1> <col2> ...", "Display only the selected columns")
    table.add_row(
        "unique <column> [--count]",
        "List unique values of a column (optionally with counts)",
    )
    table.add_row(
        "value_counts <column> [--normalize]",
        "Show frequency distribution of a column",
    )

    table.add_row("", "")

    # ── Aggregation & Statistics ─────────────────────
    section(table, "Aggregation & Statistics")
    table.add_row("describe [col...]", "Statistical summary of numeric columns")
    table.add_row(
        "groupby <group_col...> <agg_column> <agg_func>",
        "Group data and aggregate (count, mean, sum, min, max)",
    )

    table.add_row("", "")

    # ── Visualization ────────────────────────────────
    section(table, "Visualization")
    table.add_row(
        "barplot <column>",
        "Bar plot for categorical columns (≤ 20 unique values)",
    )
    table.add_row(
        "hist <column> [bins]",
        "Histogram for a numeric column (default bins: 10)",
    )
    table.add_row(
        "lineplot <x_column> <y_column> [--agg mean|sum|min|max|count]",
        "Line plot of aggregated y-values against x-values",
    )
    table.add_row(
        "heatmap <x_column> <y_column> [value_column] [--bins N]",
        "Heatmap showing density or aggregated values",
    )

    console.print(table)
