import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.title.string if soup.title else "No Title"
    
    # Extracting some text from the page content
    paragraphs = soup.find_all('p')
    content = ' '.join([p.get_text() for p in paragraphs][:3])  # taking first 3 paragraphs as content
    
    return {
        "Title": title,
        "Content": content,
        "URL": url
    }

# Read URLs from Excel file
input_file = 'Scrapping Python Assignment- Flair Insights.xlsx'  # Replace with your Excel file name
output_file = 'scraped_data.xlsx'  # Output Excel file name

try:
    df = pd.read_excel(input_file)
    urls = df['URLs'].tolist()
    
    # Scraping the data
    scraped_data = [scrape_url(url) for url in urls]
    
    # Create a DataFrame from the scraped data
    scraped_df = pd.DataFrame(scraped_data)
    
    # Write the scraped data to Excel file
    scraped_df.to_excel(output_file, index=False, engine='openpyxl')
    
    print(f"Data has been scraped and saved to '{output_file}'")
    
except Exception as e:
    print(f"An error occurred: {e}")
