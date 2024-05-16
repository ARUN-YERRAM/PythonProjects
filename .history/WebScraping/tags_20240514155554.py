import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())
print(soup.title.string,type(soup.title.string))


print(soup.div)

print(soup.find_all("div")[1])

print(soup.get("href"))

print(soup.select("div.italic"))


for child in soup.find(class_="container").children:
    print(child)

for parent in soup.find(class_="box").parents:
    print(parent)

cnt = soup.find(class_="container")
cnt.name="span"
cnt["class"] = "myclass"
cnt.string = "I am a string"
print(cnt)


uTag = soup.new_tag("ul")
liTag = soup.new_tag("li")

liTag.string = "Home"
uTag.append(liTag)


uTag = soup.new_tag("ul")
liTag = soup.new_tag("li")

liTag.string = "About"
uTag.append(liTag)

soup.html.body.insert(0,uTag)
with open("modified.html","w") as f:
    f.write(str(soup))

