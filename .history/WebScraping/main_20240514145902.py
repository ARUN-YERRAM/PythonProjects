import requests

url = "https://timesofindia.indiatimes.com/technology"

r = requests.get(url)
print(r.text)


