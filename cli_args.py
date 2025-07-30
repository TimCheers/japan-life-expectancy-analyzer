import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Life Expectancy Data Analyzer")
    parser.add_argument("--file", type=str, help="Path to CSV file", required=True)
    parser.add_argument("--show-columns", action="store_true", help="Show column names")
    parser.add_argument("--show-sample", action="store_true", help="Show first rows")
    parser.add_argument("--analyze", action="store_true", help="Analyze data")
    return parser.parse_args()
