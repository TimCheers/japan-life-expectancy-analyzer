from utils.logger import get_logger
from utils.reader import read_csv_file
from utils.analysis import analyze_dataframe, show_columns, show_sample, show_analysis
from rich.console import Console
from cli_args import parse_args

logger = get_logger()
console = Console()
args = parse_args()

def main():
    logger.info("Starting analysis script")
    df = read_csv_file(args.file)

    if df is None:
        logger.error("DataFrame is None — exiting.")
        return

    if args.show_columns:
        logger.info("Showing columns")
        show_columns(df)

    if args.show_sample:
        logger.info("Showing sample")
        show_sample(df)

    if args.analyze:
        logger.info("Analyzing dataset")
        result = analyze_dataframe(df)
        show_analysis(result)

    logger.info("Finished")

#python -m cli.main --file data/japan_life_expectancy.csv --*show-columns --show-sample --analyze
if __name__ == "__main__":
    main()
