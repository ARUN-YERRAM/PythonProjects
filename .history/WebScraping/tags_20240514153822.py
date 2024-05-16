import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())
print(soup.title.string,type(soup.title.string))


print(soup.div)

print(soup.find_all("div")[1])

print(soup.get("href"))
-- {'ip': '49.204.104.41'}
print(soup.select("div.italic"))