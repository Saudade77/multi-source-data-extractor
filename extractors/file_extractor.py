import pandas as pd
from utils.logger import setup_logger

logger = setup_logger("file_extractor")


def extract_from_file(file_path: str) -> pd.DataFrame:
    """
    Read data from a CSV or Excel file.
    
    Args:
        file_path: Path to the file.
    
    Returns:
        A DataFrame containing the file data.
    """
    logger.info(f"Reading file: {file_path}")

    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith((".xlsx", ".xls")):
            df = pd.read_excel(file_path)
        else:
            logger.error(f"Unsupported file format: {file_path}")
            return pd.DataFrame()

        df["source"] = "file"
        logger.info(f"File reading completed, total {len(df)} records")
        return df

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        logger.error(f"Failed to read file: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    # Create a sample CSV for testing
    test_df = pd.DataFrame(
        {
            "title": ["Book A", "Book B", "Book C"],
            "price": ["£10.00", "£15.50", "£8.99"],
            "stock_status": ["In stock", "In stock", "Out of stock"],
            "rating": ["Four", "Five", "Three"],
        }
    )
    test_df.to_csv("output/sample_data.csv", index=False)

    df = extract_from_file("output/sample_data.csv")
    print(df)