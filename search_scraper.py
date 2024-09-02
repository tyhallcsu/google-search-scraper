import requests
from bs4 import BeautifulSoup
import time
import random
import re
import csv
import argparse
import logging
from urllib.parse import urlparse

def setup_logger(log_level):
    """Set up and configure logger."""
    logging.basicConfig(level=log_level,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    return logging.getLogger(__name__)

def search_google(query, start=0, num_results=10, user_agent=None):
    """Perform a Google search and return the BeautifulSoup object of the result page."""
    url = f"https://www.google.com/search?q={query}&start={start}&num={num_results}"
    headers = {'User-Agent': user_agent or 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        logger.info(f"Successfully fetched page {start // num_results + 1}")
    else:
        logger.error(f"Failed to fetch page {start // num_results + 1}, status code: {response.status_code}")
    return BeautifulSoup(response.text, 'html.parser')

def extract_info(soup, domain):
    """Extract relevant information from the search results."""
    info = []
    for div in soup.find_all('div', class_='g'):
        title_div = div.find('h3', class_='r')
        if title_div:
            title = title_div.text.strip()
        else:
            title = "No title found"

        url_div = div.find('div', class_='yuRUbf')
        if url_div and url_div.find('a'):
            url = url_div.find('a')['href']
            if domain in url:
                match = re.search(rf'https?://(?:www\.)?{re.escape(domain)}[^\s&]+', url)
                if match:
                    url = match.group(0)
                    
                    desc_div = div.find('div', class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf')
                    description = desc_div.text.strip() if desc_div else "No description found"
                    
                    info.append((title, url, description))

    return info

def scrape_all_results(query, domain, max_pages=50, delay=2, output_file='scraped_info.csv'):
    """Scrape all results from Google search."""
    all_info = []
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Title', 'URL', 'Description'])

        for page in range(max_pages):
            start = page * 10
            logger.info(f"Fetching page {page + 1}...")
            soup = search_google(query, start)
            page_info = extract_info(soup, domain)
            
            if not page_info:
                logger.info(f"No information found on page {page + 1}, stopping search.")
                break
            
            for info in page_info:
                if info not in all_info:
                    all_info.append(info)
                    logger.info(f"Found new entry: {info[1]}")
                    csv_writer.writerow(info)
            
            logger.info(f"Found {len(all_info)} unique entries so far...")
            time.sleep(random.uniform(delay, delay * 1.5))
    
    return all_info

def main():
    parser = argparse.ArgumentParser(description='Scrape Google search results for a specific domain.')
    parser.add_argument('query', help='The search query to use')
    parser.add_argument('domain', help='The domain to filter results for')
    parser.add_argument('-o', '--output', default='scraped_info.csv', help='Output CSV file name')
    parser.add_argument('-m', '--max-pages', type=int, default=50, help='Maximum number of pages to scrape')
    parser.add_argument('-d', '--delay', type=float, default=2, help='Delay between requests in seconds')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    parser.add_argument('-u', '--user-agent', help='Custom User-Agent string')

    args = parser.parse_args()

    global logger
    logger = setup_logger(logging.DEBUG if args.verbose else logging.INFO)

    logger.info("Starting scrape...")
    all_info = scrape_all_results(args.query, args.domain, args.max_pages, args.delay, args.output)
    logger.info(f"Finished. Found a total of {len(all_info)} unique entries and saved them to {args.output}")

if __name__ == "__main__":
    main()
