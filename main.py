import requests
from bs4 import BeautifulSoup

def proverkluch(x,y):
    for i in range(len(x)):
        if x[i] not in y: return False #проверка ключей осуществляется в формате "и"
    return True

k = 0
kluch = ["Поддержка","Гранты"] #ключевое слово/массив слов
urlmas = ["https://mbkuban.ru/documents/gosudarstvennaya-programma/","https://xn--90aifddrld7a.xn--p1ai/anticrisis/","https://admkrai.krasnodar.ru/*https://moibiz93.ru/","https://mbkuban.ru/","https://dirmsp.krasnodar.ru/activity/msp"]

for url in urlmas:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title
    links = soup.find_all("a")
    for link in links:
        try:
            if "http" in (link.get("href")) :
                url1 = f'{link.get("href")}'
                response1 = requests.get(url1)
                bit = BeautifulSoup(response1.text, "html.parser")
                text = bit.get_text(strip=True)
            if (k==1) and proverkluch(kluch,text):
                    with open(r'data.txt', 'a', encoding='utf-8') as data:
                        data.write("$"+f"{text}"+"$")
            elif proverkluch(kluch,text):
                    with open(r'data.txt', 'w', encoding='utf-8') as data:
                        data.write("$"+f"{text}"+"$")
                        k = 1
        except:
                ...

