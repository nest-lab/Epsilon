import requests
from bs4 import BeautifulSoup

links = []
input_search_words = (raw_input("Enter a string: "))
url = "https://www.google.com.ng/search?q=" + input_search_words
response = requests.get(url)
soup = str(BeautifulSoup(response.content))

def getURL(page):
    start_link = soup.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

while True:
    url, n = getURL(soup)
    soup = soup[n:]
    if url:
        links.append(url)
        for i in links:
            if "https://" in i:
                print i
    else:
        break