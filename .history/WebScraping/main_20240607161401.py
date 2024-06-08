import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

try:
    # Fetch the webpage content
    r = requests.get(url)
    r.raise_for_status()  # Raise an HTTPError for bad responses
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# Get the prettified HTML content
html_content = soup.prettify()

# Save the HTML content to a file named 'bbc.html'
with open("bbc.html", "w", encoding="utf-8") as file:
    file.write(html_content)

# Print the first <div> element
print(soup.find("div"))

print("HTML content saved to bb.html")
