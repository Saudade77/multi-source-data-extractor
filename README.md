直接复制以下全部内容，粘贴到 README.md 文件中：
markdownDownloadCopy code# Multi-Source Data Extractor

A production-ready Python ETL pipeline that extracts data from multiple sources (websites, APIs, files), performs data cleaning and validation, then exports to CSV, Excel, or Google Sheets.

## Features

**Data Extraction**
- Web scraping with BeautifulSoup (pagination support)
- REST API integration with JSON handling
- Local file reading (CSV, Excel)

**Data Processing**
- Duplicate removal
- Price standardization (currency symbol stripping)
- Rating conversion (text to numeric)
- Data validation with quality flags

**Export Options**
- CSV with UTF-8 encoding
- Excel with auto-resized columns
- Google Sheets (optional, requires credentials)

**Production Ready**
- Comprehensive logging (console + file)
- JSON configuration (no code changes needed)
- Graceful error handling (404s, missing files, malformed data)

## Quick Start

**1. Clone and Setup**

```bash
git clone https://github.com/YOUR_USERNAME/multi-source-data-extractor.git
cd multi-source-data-extractor
python -m venv venv
2. Activate Virtual Environment
bashDownloadCopy code# Windows PowerShell
venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate.bat

# Linux / macOS
source venv/bin/activate
3. Install Dependencies
bashDownloadCopy codepip install -r requirements.txt
4. Run
bashDownloadCopy codepython main.py
Demo Output
INFO - Multi-Source Data Extractor Started
INFO - Scraping page 1: https://books.toscrape.com/index.html
INFO - Page 1 completed, extracted 20 books
INFO - Scraping page 2: https://books.toscrape.com/catalogue/page-2.html
INFO - Page 2 completed, extracted 20 books
INFO - Website scraping completed, total 40 records
INFO - API extraction completed, total 10 records
INFO - File reading completed, total 3 records
INFO - All sources combined, total 53 records
INFO - Data cleaning completed, final records: 53
INFO - CSV export successful: output/result.csv
INFO - Excel export successful: output/result.xlsx
INFO - Task Completed!

Sample Data Output
titleprice_cleanrating_numericsourceis_validA Light in the Attic51.773websiteTrueTipping the Velvet53.741websiteTrueLeanne GrahamNaNNaNapiFalseBook A10.004fileTrue
Configuration
Edit config.json to customize sources and exports:
jsonDownloadCopy code{
  "sources": [
    {
      "type": "website",
      "url": "https://books.toscrape.com/index.html",
      "max_pages": 2
    },
    {
      "type": "api",
      "url": "https://jsonplaceholder.typicode.com/users"
    },
    {
      "type": "file",
      "path": "output/sample_data.csv"
    }
  ],
  "export": {
    "csv": {
      "enabled": true,
      "path": "output/result.csv"
    },
    "excel": {
      "enabled": true,
      "path": "output/result.xlsx"
    },
    "gsheet": {
      "enabled": false,
      "credentials_path": "credentials.json",
      "spreadsheet_name": "Extracted Data"
    }
  }
}
Project Structure
multi-source-data-extractor/
├── extractors/
│   ├── web_extractor.py      # Website scraping
│   ├── api_extractor.py      # REST API calls
│   └── file_extractor.py     # CSV/Excel reading
├── processors/
│   └── cleaner.py            # Data cleaning
├── exporters/
│   ├── csv_exporter.py       # CSV export
│   ├── excel_exporter.py     # Excel export
│   └── gsheet_exporter.py    # Google Sheets export
├── utils/
│   └── logger.py             # Logging setup
├── output/                   # Generated files
├── main.py                   # Entry point
├── config.json               # Configuration
├── requirements.txt          # Dependencies
└── README.md

Tech Stack

* Python 3.8+
* Pandas (data manipulation)
* Requests (HTTP client)
* BeautifulSoup4 (HTML parsing)
* OpenPyXL (Excel export)
* GSpread (Google Sheets API)

Google Sheets Setup (Optional)

1. Go to Google Cloud Console
2. Create a new project
3. Enable Google Sheets API
4. Create a Service Account and download JSON key
5. Save as credentials.json in project root
6. Share your Google Sheet with the service account email
7. Set gsheet.enabled to true in config.json

Use Cases

* E-commerce price monitoring
* Lead generation from multiple sources
* Data aggregation for reporting
* Automated data collection pipelines
* API data backup to spreadsheets

License
MIT License - Free for personal and commercial use.
Author
Built for data extraction and ETL tasks. Deployable to AWS Lambda, Google Cloud Functions, or Apache Airflow.
