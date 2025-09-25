 News Scraper--

A simple Python script to scrape headlines from any news website and save them in a text file.
 Features:
- Extracts headlines from <h1>, <h2>, <h3>, and <title> tags.
- Saves results to headlines.txt.
- Easy to change the news website URL.

Requirements:
- Python 3.x  
- requests and beautifulsoup4  
```bash
pip install requests beautifulsoup4

Usage:

1. Set the URL in news_scraper.py:

news_url = "https://www.bbc.com/news"

2. Run:

python news_scraper.py

3. Check headlines.txt for the output.

Example Output

1. Ukraine conflict: Latest updates
2. Global markets react to new policies
3. Climate change warnings



