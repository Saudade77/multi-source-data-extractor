import pandas as pd
import re
from utils.logger import setup_logger

logger = setup_logger("cleaner")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and validate the data.
    
    Args:
        df: The raw DataFrame to clean.
    
    Returns:
        A cleaned DataFrame with additional validation columns.
    """
    logger.info(f"Starting data cleaning, original records: {len(df)}")

    # 1. Remove duplicate rows
    original_count = len(df)
    df = df.drop_duplicates()
    if len(df) < original_count:
        logger.info(f"Deduplication: removed {original_count - len(df)} duplicate records")

    # 2. Parse price field (if exists)
    if "price" in df.columns:
        df["price_clean"] = df["price"].apply(parse_price)
        logger.info("Price field cleaned")

    # 3. Convert rating to numeric (if exists)
    if "rating" in df.columns:
        rating_map = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
            "Unknown": None,
        }
        df["rating_numeric"] = df["rating"].map(rating_map)
        logger.info("Rating field converted to numeric")

    # 4. Strip whitespace from string columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()

    # 5. Mark data validity
    df["is_valid"] = True

    # Validation: title should not be empty
    if "title" in df.columns:
        invalid_title = df["title"].isin(["", "nan", "None"])
        df.loc[invalid_title, "is_valid"] = False
        invalid_count = invalid_title.sum()
        if invalid_count > 0:
            logger.warning(f"Found {invalid_count} records with empty titles")

    logger.info(f"Data cleaning completed, final records: {len(df)}")
    return df


def parse_price(price_str: str) -> float:
    """
    Extract numeric value from a price string.
    
    Example: "£51.77" -> 51.77
    
    Args:
        price_str: The price string to parse.
    
    Returns:
        The numeric price value, or None if parsing fails.
    """
    if pd.isna(price_str):
        return None
    match = re.search(r"[\d.]+", str(price_str))
    if match:
        return float(match.group())
    return None


if __name__ == "__main__":
    # Test run
    test_df = pd.DataFrame(
        {
            "title": ["Book A", "Book B", "Book B", "  ", "Book C"],
            "price": ["£10.00", "£15.50", "£15.50", "£5.00", "invalid"],
            "rating": ["Four", "Five", "Five", "Three", "Unknown"],
        }
    )
    cleaned = clean_data(test_df)
    print(cleaned)