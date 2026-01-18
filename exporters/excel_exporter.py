import pandas as pd
import os
from utils.logger import setup_logger

logger = setup_logger("excel_exporter")


def export_to_excel(
    df: pd.DataFrame, output_path: str, sheet_name: str = "Data"
) -> bool:
    """
    Export DataFrame to an Excel file with basic formatting.
    
    Args:
        df: The DataFrame to export.
        output_path: The output file path.
        sheet_name: The name of the worksheet.
    
    Returns:
        True if export succeeded, False otherwise.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)

            # Auto-adjust column widths
            worksheet = writer.sheets[sheet_name]
            for idx, col in enumerate(df.columns):
                max_length = max(df[col].astype(str).map(len).max(), len(col)) + 2
                column_letter = chr(65 + idx) if idx < 26 else f"A{chr(65 + idx - 26)}"
                worksheet.column_dimensions[column_letter].width = min(max_length, 50)

        logger.info(f"Excel export successful: {output_path}")
        return True
    except Exception as e:
        logger.error(f"Excel export failed: {e}")
        return False