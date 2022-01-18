from bs4 import BeautifulSoup
import requests

response = requests.get("https://filmix.ac/")
bs = BeautifulSoup(response.content, 'html.parser')
articles = bs.select('article.shortstory')
for article in articles:
    link = article.select('h2.name > a.btn-tooltip')
    print(link[0].get_text())