"""
Install beautifulsoup and requests -
pip install beautifulsoup4 requests
"""

# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

# The URL of the website we want to scrape
URL = "http://quotes.toscrape.com/"

# Sending an HTTP request to the URL
page = requests.get(URL)

# Parsing the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Finding all the <span> elements that have a class "text"
# These elements contain the quotes we want to scrape
quotes = soup.findAll("span", class_="text")

# Looping through each quote element found
for quote in quotes:
    # Printing the text content of each quote
    # .text extracts the text part of the HTML element
    print(quote.text)