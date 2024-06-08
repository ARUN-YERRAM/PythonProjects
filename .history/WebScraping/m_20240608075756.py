from bs4 import BeautifulSoup
import requests
import csv
url = "https://www.bbc.com/news"

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

elements = soup.find_all(["h2", "a"])

with open('headlines.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'URL'])
    
    for element in elements:
        headline_text = element.text.strip()
        headline_url = element.get('href')
        writer.writerow([headline_text, headline_url])
    
print("Data scraping complete and saved to headlines;csv.")