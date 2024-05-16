import requests

proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080"
}
r = requests.get("https://api64.ipify.org?format=json")

print(r.json())
-- {'ip': '49.204.104.41'}
print(soup.select("div.italic"))