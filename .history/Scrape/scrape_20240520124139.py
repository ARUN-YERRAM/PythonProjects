from bs4 import BeautifulSoup
import requests

try:
    response = requests.get('https://coreyms.com')
    response.raise_for_status()  # Check for request errors
except requests.exceptions.RequestException as e:
    print(f'Error during requests to coreyms.com: {e}')
    exit()

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())  # Use prettify to print the soup nicely formatted
