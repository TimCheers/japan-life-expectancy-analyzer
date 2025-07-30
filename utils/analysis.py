from rich.table import Table
from rich.console import Console

console = Console()

def show_columns(df):
    table = Table(title="Columns")
    table.add_column("Column Name", style="cyan")
    for col in df.columns:
        table.add_row(col)
    console.print(table)

def show_sample(df, n=5):
    table = Table(title=f"First {n} Rows")
    for col in df.columns:
        table.add_column(str(col), overflow="fold")
    for _, row in df.head(n).iterrows():
        table.add_row(*[str(val) for val in row])
    console.print(table)

def analyze_dataframe(df):
    result = {}
    numeric_df = df.select_dtypes(include="number")
    for col in numeric_df.columns:
        result[col] = {
            "mean": round(numeric_df[col].mean(), 2),
            "min": round(numeric_df[col].min(), 2),
            "max": round(numeric_df[col].max(), 2)
        }
    return result

def show_analysis(result):
    table = Table(title="Data Analysis")
    table.add_column("Column", style="cyan")
    table.add_column("Mean")
    table.add_column("Min")
    table.add_column("Max")

    for col, stats in result.items():
        table.add_row(col, str(stats["mean"]), str(stats["min"]), str(stats["max"]))

    console.print(table)
