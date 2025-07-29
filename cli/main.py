import argparse
import pandas as pd
from rich.console import Console
from rich.table import Table
from pathlib import Path

console = Console()

def load_csv(path):
    if not Path(path).exists():
        console.print(f"[red]Файл не найден: {path}[/red]")
        return None
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        console.print(f"[red]Ошибка загрузки CSV: {e}[/red]")
        return None

def show_columns(df):
    table = Table(title="Колонки CSV-файла")
    table.add_column("№")
    table.add_column("Имя колонки")
    for i, col in enumerate(df.columns):
        table.add_row(str(i), col)
    console.print(table)

def show_sample(df, n=5):
    console.print(df.head(n).to_string(index=False))

def main():
    parser = argparse.ArgumentParser(description="CLI для анализа данных")
    parser.add_argument("--file", type=str, required=True, help="Путь к CSV-файлу")
    args = parser.parse_args()

    df = load_csv(args.file)
    if df is not None:
        show_columns(df)
        show_sample(df)

if __name__ == "__main__":
    main()