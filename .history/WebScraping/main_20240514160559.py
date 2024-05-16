import requests
from bs4 import BeautifulSoup


url = "https://timesofindia.indiatimes.com/technology"
fetchAndSaveToFile(url, "data/times.html")

r = requests.get(url)
print(r.text)
