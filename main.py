import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import concurrent.futures

WebUrl = input("Enter URL String: ")
links = []


def getImageLinks(URL):
    r = requests.get(URL)
    print(r.status_code)
    soup = BeautifulSoup(r.text, "html.parser")
    Images = soup.find_all("img")
    for img in Images:
        if img.has_key("src"):
            link = img["src"]
        if link.endswith(".png"):
            links.append(link)
    return


# print(len(links))
try:
    os.mkdir("images")
except:
    pass


def DownloadImage(URL):
    name = URL.split("/")[len(URL.split("/")) - 1]
    name = "images/" + name
    data = requests.get(URL)
    with open(name, "wb") as f:
        f.write(data.content)
    print(name)
    return


now = datetime.now()
getImageLinks(WebUrl)

# 0:01:10.758931
for L in links:
    try:
        DownloadImage(L)
    except:
        pass

# with concurrent.futures.Executor() as executor:
#    map(DownloadImage,links)

print(datetime.now() - now)
