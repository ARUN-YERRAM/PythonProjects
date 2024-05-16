import requests
from bs4 import BeautifulSoup

proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080"
}


url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"


r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')
spans = soup.select("s2")
print(soup.find_all("div"))

