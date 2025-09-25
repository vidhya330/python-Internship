# news_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file="headlines.txt"):
    try:
        
        response = requests.get(url)
        response.raise_for_status()  

        
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all(["h1", "h2", "h3", "title"])  

        
        with open(output_file, "w", encoding="utf-8") as file:
            for idx, headline in enumerate(headlines, start=1):
                text = headline.get_text(strip=True)
                if text: 
                    file.write(f"{idx}. {text}\n")

        print(f" Headlines saved successfully in '{output_file}'")

    except requests.exceptions.RequestException as e:
        print(f" Error fetching the website: {e}")


if __name__ == "__main__":
    news_url = "https://www.bbc.com/news"   
    scrape_headlines(news_url)
