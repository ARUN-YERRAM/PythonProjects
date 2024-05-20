from bs4 import beautifulSoup
import requests
source = requests.get('http://coreyms.com').text
soup = beautifulSoup(source, 'lxml')
article = soup.find('article')

print(article.prettify())