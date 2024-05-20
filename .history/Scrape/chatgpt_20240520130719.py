from bs4 import BeautifulSoup
import requests
import csv

# URL of the page we want to scrape
url = 'https://www.python.org/blogs/'

# Send a GET request to the page
try:
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')
    exit()

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Open a CSV file to write the scraped data
with open('python_blogs_scrape.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline', 'summary', 'link'])

    # Loop through all articles on the page
    for article in soup.find_all('li', class_='list-recent-posts menu'):
        # Extract the headline
        headline = article.h2.a.text.strip()
        print(f'Headline: {headline}')

        # Extract the summary (first few words of the content)
        summary = article.find('p').text.strip()
        print(f'Summary: {summary}')

        # Extract the link to the full article
        link = article.h2.a['href']
        full_link = f'https://www.python.org{link}'
        print(f'Link: {full_link}')

        # Write the data to the CSV file
        csv_writer.writerow([headline, summary, full_link])

        print()  # Print a newline for better readability in the output
