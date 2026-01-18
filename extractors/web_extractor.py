import requests
from bs4 import BeautifulSoup
import pandas as pd
from utils.logger import setup_logger

logger = setup_logger("web_extractor")

def extract_from_website(url: str, max_pages: int = 3) -> pd.DataFrame:
    """
    Extract book data from books.toscrape.com.
    """
    all_books = []
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    
    for page in range(1, max_pages + 1):
        # Use correct pagination URL format
        if page == 1:
            page_url = url
        else:
            page_url = base_url.format(page)
        
        logger.info(f"Scraping page {page}: {page_url}")
        
        try:
            response = requests.get(page_url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            continue
        
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.select("article.product_pod")
        
        for book in books:
            title = book.select_one("h3 a")["title"]
            price = book.select_one("p.price_color").text
            stock = book.select_one("p.instock.availability")
            stock_status = stock.text.strip() if stock else "Unknown"
            rating_tag = book.select_one("p.star-rating")
            rating = rating_tag["class"][1] if rating_tag else "Unknown"
            
            all_books.append({
                "title": title,
                "price": price,
                "stock_status": stock_status,
                "rating": rating,
                "source": "website"
            })
        
        logger.info(f"Page {page} completed, extracted {len(books)} books")
    
    logger.info(f"Website scraping completed, total {len(all_books)} records")
    return pd.DataFrame(all_books)


if __name__ == "__main__":
    # Test run
    url = "https://books.toscrape.com/index.html"
    df = extract_from_website(url, max_pages=2)
    print(df.head())