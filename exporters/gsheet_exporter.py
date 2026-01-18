import pandas as pd
from utils.logger import setup_logger

logger = setup_logger("gsheet_exporter")


def export_to_gsheet(
    df: pd.DataFrame, credentials_path: str, spreadsheet_name: str
) -> bool:
    """
    Export DataFrame to Google Sheets.
    
    Requires a Google Cloud service account with appropriate permissions.
    
    Args:
        df: The DataFrame to export.
        credentials_path: Path to the service account JSON file.
        spreadsheet_name: Name of the Google Spreadsheet.
    
    Returns:
        True if export succeeded, False otherwise.
    """
    try:
        import gspread
        from gspread_dataframe import set_with_dataframe

        gc = gspread.service_account(filename=credentials_path)

        try:
            spreadsheet = gc.open(spreadsheet_name)
        except gspread.SpreadsheetNotFound:
            spreadsheet = gc.create(spreadsheet_name)
            logger.info(f"Created new spreadsheet: {spreadsheet_name}")

        worksheet = spreadsheet.sheet1
        worksheet.clear()
        set_with_dataframe(worksheet, df)

        logger.info(f"Google Sheets export successful: {spreadsheet_name}")
        logger.info(f"URL: {spreadsheet.url}")
        return True

    except ImportError:
        logger.error("Please install gspread: pip install gspread gspread-dataframe")
        return False
    except Exception as e:
        logger.error(f"Google Sheets export failed: {e}")
        return False