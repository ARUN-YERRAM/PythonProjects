import requests

proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080"
}
r = requests.get("https://api64.ipify.org?format=json")

print(r.json())
print(soup.get("href"))
-- {'ip': '49.204.104.41'}
print(soup.select("div.italic"))
prinr(soup.select("span#italic"))
print(soup.span.get("class"))
print(soup.find(id="first"))
