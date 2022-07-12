from bs4 import BeautifulSoup
import requests

content = requests.get('https://ru.ufes.br/cardapio').text

soup = BeautifulSoup(content, 'lxml')
tags = soup.find_all('p')
for tag in tags:
    print(tag.text)
