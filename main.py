import json
import pandas as pd
from extractors.web_extractor import extract_from_website
from extractors.api_extractor import extract_from_api
from extractors.file_extractor import extract_from_file
from processors.cleaner import clean_data
from exporters.csv_exporter import export_to_csv
from exporters.excel_exporter import export_to_excel
from exporters.gsheet_exporter import export_to_gsheet
from utils.logger import setup_logger

logger = setup_logger("main")


def load_config(config_path: str = "config.json") -> dict:
    """Load configuration from a JSON file."""
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_all(sources: list) -> pd.DataFrame:
    """
    Extract data from all configured sources.
    
    Args:
        sources: List of source configurations.
    
    Returns:
        A combined DataFrame containing data from all sources.
    """
    all_data = []

    for source in sources:
        source_type = source.get("type")
        logger.info(f"Starting extraction from {source_type}...")

        if source_type == "website":
            df = extract_from_website(
                url=source["url"], max_pages=source.get("max_pages", 3)
            )
        elif source_type == "api":
            df = extract_from_api(url=source["url"], params=source.get("params"))
        elif source_type == "file":
            df = extract_from_file(source["path"])
        else:
            logger.warning(f"Unknown source type: {source_type}")
            continue

        if not df.empty:
            all_data.append(df)

    if all_data:
        combined = pd.concat(all_data, ignore_index=True)
        logger.info(f"All sources combined, total {len(combined)} records")
        return combined

    return pd.DataFrame()


def export_all(df: pd.DataFrame, export_config: dict):
    """
    Export data to all enabled destinations.
    
    Args:
        df: The DataFrame to export.
        export_config: Export configuration dictionary.
    """
    if export_config.get("csv", {}).get("enabled"):
        export_to_csv(df, export_config["csv"]["path"])

    if export_config.get("excel", {}).get("enabled"):
        export_to_excel(df, export_config["excel"]["path"])

    if export_config.get("gsheet", {}).get("enabled"):
        export_to_gsheet(
            df,
            export_config["gsheet"]["credentials_path"],
            export_config["gsheet"]["spreadsheet_name"],
        )


def main():
    """Main entry point for the data extraction pipeline."""
    logger.info("=" * 50)
    logger.info("Multi-Source Data Extractor Started")
    logger.info("=" * 50)

    # 1. Load configuration
    config = load_config()

    # 2. Extract data from all sources
    raw_data = extract_all(config["sources"])

    if raw_data.empty:
        logger.error("No data extracted, exiting")
        return

    # 3. Clean and validate data
    cleaned_data = clean_data(raw_data)

    # 4. Export data to all enabled destinations
    export_all(cleaned_data, config["export"])

    logger.info("=" * 50)
    logger.info("Task Completed!")
    logger.info("=" * 50)


if __name__ == "__main__":
    main()