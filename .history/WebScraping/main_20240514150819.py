import requests


def fetchAndSaveToFile(url,path):
    r = requests.get(url)
    with open("data/times.html", "w", encoding="utf-8", errors="ignore") as f:
    f.write(r.text)

    


url = "https://timesofindia.indiatimes.com/technology"

fetchAndSaveToFile(url,"data/times.html")

r = requests.get(url)
print(r.text)


