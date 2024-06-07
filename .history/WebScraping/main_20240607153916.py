import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080"
}

url = "https://www.bbc.com/news"


r = requests.get(url, proxies=proxies)

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

# Get the prettified HTML content
html_content = soup.prettify()

# Save the HTML content to a file named 'bbc.html'
with open("bbc.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML content saved to bbc.html")

soup = BeautifulSoup(r.text, 'html.parser')


print(soup.prettify())
