import pandas as pd
import os
from utils.logger import setup_logger

logger = setup_logger("csv_exporter")


def export_to_csv(df: pd.DataFrame, output_path: str) -> bool:
    """
    Export DataFrame to a CSV file.
    
    Args:
        df: The DataFrame to export.
        output_path: The output file path.
    
    Returns:
        True if export succeeded, False otherwise.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False, encoding="utf-8-sig")
        logger.info(f"CSV export successful: {output_path}")
        return True
    except Exception as e:
        logger.error(f"CSV export failed: {e}")
        return False