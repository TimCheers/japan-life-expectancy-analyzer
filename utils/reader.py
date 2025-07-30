import pandas as pd
from rich.console import Console

console = Console()

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        console.print(f"[green]Loaded file:[/green] {file_path}")
        return df
    except FileNotFoundError:
        console.print(f"[red]File not found:[/red] {file_path}")
    except Exception as e:
        console.print(f"[red]Error reading file:[/red] {e}")
    return None
