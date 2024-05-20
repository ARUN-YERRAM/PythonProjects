from bs4 import BeautifulSoup
import requests
import csv

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

match = soup.find_all('div' , class_='footer')

print(match.p.text)

