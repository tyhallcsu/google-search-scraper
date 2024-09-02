
# Google Search Scraper

This Python script allows you to scrape Google search results for a specific domain. It's useful for SEO analysis, content auditing, and general web research.

## Features

- Scrape Google search results for a specified domain
- Customize search parameters (query, max pages, delay between requests)
- Output results to a CSV file
- Configurable User-Agent string
- Verbose logging option

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/tyhallcsu/google-search-scraper.git
   cd google-search-scraper
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line with the following syntax:

```
python search_scraper.py <query> <domain> [options]
```

### Arguments:

- `query`: The search query to use (e.g., "site:example.com")
- `domain`: The domain to filter results for (e.g., "example.com")

### Options:

- `-o, --output`: Output CSV file name (default: scraped_info.csv)
- `-m, --max-pages`: Maximum number of pages to scrape (default: 50)
- `-d, --delay`: Delay between requests in seconds (default: 2)
- `-v, --verbose`: Enable verbose logging
- `-u, --user-agent`: Custom User-Agent string

### Example:

```
python search_scraper.py "site:example.com" "example.com" -o results.csv -m 10 -d 3 -v
```

This command will:
- Search for "site:example.com"
- Filter results for "example.com"
- Output results to "results.csv"
- Scrape up to 10 pages
- Wait 3 seconds between requests
- Use verbose logging

## Output

The script generates a CSV file with the following columns:
1. Title
2. URL
3. Description

## Disclaimer

Web scraping may be against the terms of service of some websites. Use this tool responsibly and ensure you have the right to scrape the target website. The authors are not responsible for any misuse of this tool.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/google-search-scraper/issues).

## License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.


## Changelog / Updates

### v2.0

This updated script includes:

1. More verbose logging throughout the script, especially in the `extract_info` function.
2. A new `--urls-only` argument that, when set, will only export URLs to the CSV file.
3. Additional logging in the `main` function to show the parameters being used for the scrape.

To use the script with these new features:

- For verbose logging:
  ```
  python search_scraper.py "site:example.com" "example.com" -v
  ```

- To export only URLs:
  ```
  python search_scraper.py "site:example.com" "example.com" --urls-only
  ```

These changes provide more detailed logging for debugging purposes and offer more flexibility in the output format.
The verbose logging will help you understand exactly what the script is doing at each step, which can be particularly useful when troubleshooting or when you want to know why specific results are or aren't being included.

### v3.0

The main changes are:

1. Modified the `setup_logger` function to accept a `log_file` parameter.
2. Added a file handler to the logger if a log file is specified.
3. Added a new command-line argument `-l` or `--log-file` to specify the log file.

Now you can use the script with file logging like this:

```
python3 search_scraper.py "site:example.com" "example.com" -o scrape_example.csv -m 500 -d 3 -v --urls-only -l scrape_log.txt
```

This will create a log file named `scrape_log.txt` in addition to logging to the console. The log file will contain all the verbose output, which you can review later to investigate any issues that might have occurred during scraping.

This setup allows you to have both console output for real-time monitoring and a detailed log file for later analysis, giving you the best of both worlds for debugging and investigating the scraping process.
