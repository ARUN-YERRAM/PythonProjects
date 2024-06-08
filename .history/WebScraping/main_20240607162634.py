import requests
from bs4 import BeautifulSoup

url = "https://www.timesofindia.com/news"

# Make the request without proxies
r = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# Get the prettified HTML content
html_content = soup.prettify()

# Save the HTML content to a file named 'bbc.html'
with open("bbc.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML content saved to bbc.html")