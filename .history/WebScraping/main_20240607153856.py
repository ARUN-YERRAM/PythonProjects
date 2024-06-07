import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080"
}

url = "https://www.bbc.com/news"


r = requests.get(url, proxies=proxies)


soup = BeautifulSoup(r.text, 'html.parser')


print(soup.prettify())
