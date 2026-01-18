# Multi-Source Data Extractor 🚀

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pandas](https://img.shields.io/badge/Pandas-Powered-green.svg)](https://pandas.pydata.org/)

A professional-grade **ETL (Extract, Transform, Load) pipeline** built with Python. This tool automatically extracts data from **Websites**, **REST APIs**, and **local files**, cleans the data, and exports it to **CSV**, **Excel**, or **Google Sheets**.

---

## ✨ Key Features

- **🌐 Multi-Source Extraction**
  - **Web Scraping**: Extracts product data (BeautifulSoup4) with pagination support.
  - **API Integration**: Fetches JSON data from REST endpoints.
  - **File Processing**: Reads local CSV and Excel files.

- **🧹 Data Cleaning & Validation**
  - Removes duplicate records automatically.
  - Standardizes formats (e.g., currency, ratings).
  - Handles nested JSON objects (dictionaries/lists).
  - Flags invalid or missing data.

- **📤 Flexible Export Options**
  - **CSV**: UTF-8 encoded for universal compatibility.
  - **Excel**: Auto-adjusted column widths for better readability.
  - **Google Sheets**: Direct upload via API (optional).

- **📝 Robust Logging**
  - Detailed console output and file logging with timestamps.
  - Error handling for network issues, 404s, and missing files.

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Saudade77/multi-source-data-extractor.git
cd multi-source-data-extractor