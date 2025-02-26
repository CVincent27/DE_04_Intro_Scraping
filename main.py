import requests
from bs4 import BeautifulSoup

def scraping_title(url):
    r = requests.get(url)
    bs = BeautifulSoup(r.content, "html.parser")
    # print(bs)
    title = bs.h1
    # /!\ return premier h1 seulement
    return title

title = scraping_title("https://realpython.com/beautiful-soup-web-scraper-python/")
print(title)