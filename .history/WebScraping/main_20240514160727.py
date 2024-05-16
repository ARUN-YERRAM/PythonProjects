import requests
from bs4 import BeautifulSoup

proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080"
}


url = "https://timesofindia.indiatimes.com/technology"


r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify())

