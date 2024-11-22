import requests
from bs4 import BeautifulSoup

url = "https://mbkuban.ru/documents/gosudarstvennaya-programma/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Извлечение заголовка страницы
title = soup.title.string

# Извлечение всех ссылок на странице
k = 0
links = soup.find_all("a")

for link in links:
    try:
        if "http" in (link.get("href")) :
            url1 = f'{link.get("href")}'
            response1 = requests.get(url1)
            bit = (BeautifulSoup(response1.text, "html.parser"))
            text = bit.get_text(strip=True)
            if k==1:
                with open(r'data.txt', 'a', encoding='utf-8') as data:
                    data.write(f"{text}")
            else:
                with open(r'data.txt', 'w', encoding='utf-8') as data:
                    data.write(f"{text}")
                    k = 1
    except:
        ...

