import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"


r = requests.get(url)


soup = BeautifulSoup(r.text, 'html.parser')


html_content = soup.prettify()


with open("bbc.html", "w", encoding="utf-8") as file:
    file.write(html_content)


print("HTML content saved to bbc.html")
