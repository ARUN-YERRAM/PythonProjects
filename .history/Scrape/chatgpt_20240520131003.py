from bs4 import BeautifulSoup
import requests
import csv


url = 'https://www.python.org/blogs/'


try:
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')
    exit()


soup = BeautifulSoup(response.text, 'html.parser')


with open('python_blogs_scrape.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline', 'summary', 'link'])

    
    for article in soup.find_all('li', class_='list-recent-posts menu'):
        
        headline = article.h2.a.text.strip()
        print(f'Headline: {headline}')

        
        summary = article.find('p').text.strip()
        print(f'Summary: {summary}')

      
        link = article.h2.a['href']
        full_link = f'https://www.python.org{link}'
        print(f'Link: {full_link}')

        
        csv_writer.writerow([headline, summary, full_link])

        print()  
