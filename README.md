# web-scraper


This Python script reads a list of URLs from an Excel file, scrapes the content from these URLs using BeautifulSoup, and saves the scraped data back to another Excel file.

## Prerequisites

- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl`

## Installation

1. Install the required libraries using pip:
    ```bash
    pip install requests beautifulsoup4 pandas openpyxl
    ```

## Usage

1. **Prepare Excel File**: Create an Excel file (`urls.xlsx`) containing a column named 'URLs' with the URLs you want to scrape.

    Example:
    ```
    | URLs                              |
    |-----------------------------------|
    | https://example.com/page1         |
    | https://example.com/page2         |
    | https://example.com/page3         |
    ```

2. **Run the Script**: Execute the Python script `excel_scraper.py`.

    ```bash
    python excel_scraper.py
    ```

3. **Output**: After running the script, a new Excel file (`scraped_data.xlsx`) will be created with the scraped data.

## Functionality

- The script reads URLs from the 'URLs' column of the input Excel file.
- It uses the `scrape_url` function to scrape the title and content from each URL.
- The scraped data is stored in a DataFrame and saved to a new Excel file (`scraped_data.xlsx`).

## Notes

- The script extracts the title and first three paragraphs of content from each webpage.
- If a URL fails to retrieve or is invalid, it will print a message and continue with the next URL.
- Modify the script as needed to adjust the scraping behavior or data extraction.

---
