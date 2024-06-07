import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080"
}

url = "https://www.bbc.com/news"

# Make the request using the proxies
r = requests.get(url, proxies=proxies)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# Print all the HTML content from the webpage
print(soup.prettify())
