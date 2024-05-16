import requests

proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080"
}
r = requests.get("https://api64.ipify.org?format=json")

print(r.json())
print(soup.get("href"))

print(soup.select("div.italic"))
print(soup.select("span#italic"))
print(soup.span.get("class"))
print(soup.find_all(class_="italic"))
