import requests
import pandas as pd
import json
from utils.logger import setup_logger

logger = setup_logger("api_extractor")

def extract_from_api(url: str, params: dict = None) -> pd.DataFrame:
    """
    Extract data from a REST API.
    Nested objects are converted to JSON strings.
    """
    logger.info(f"Requesting API: {url}")
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        logger.error(f"API request failed: {e}")
        return pd.DataFrame()
    except ValueError as e:
        logger.error(f"JSON parsing failed: {e}")
        return pd.DataFrame()
    
    # Convert to DataFrame
    if isinstance(data, list):
        df = pd.DataFrame(data)
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, list):
                df = pd.DataFrame(value)
                break
        else:
            df = pd.DataFrame([data])
    else:
        df = pd.DataFrame()
    
    # Convert nested dicts/lists to JSON strings (fix for drop_duplicates)
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, (dict, list))).any():
            df[col] = df[col].apply(lambda x: json.dumps(x) if isinstance(x, (dict, list)) else x)
            logger.info(f"Converted nested objects in column '{col}' to JSON strings")
    
    df["source"] = "api"
    logger.info(f"API extraction completed, total {len(df)} records")
    return df


if __name__ == "__main__":
    # Test run with a public fake data API
    url = "https://jsonplaceholder.typicode.com/users"
    df = extract_from_api(url)
    print(df.head())