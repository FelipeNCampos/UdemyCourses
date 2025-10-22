from bs4 import BeautifulSoup
import requests


with open("website.html") as file:
    content = file.read()

content = requests.get("https://environmentservices.camden.gov.uk/property/5035135")

html = content.text

# print(html)
soup = BeautifulSoup(html, 'html.parser')


msgs = soup.find_all(class_="task-state")


# print(f"0 - {msgs[0]}")


# print(f"1 - {msgs[1]}")
msgs_last_collect = []

for tag in msgs:
    # Iterando sobre os filhos diretos
    # for child in tag.children:
    #     print(child)
    # Ou acessando como lista
    # print(tag.contents)
    # Buscando uma tag específica dentro do resultado
    msgs_last_collect.append(tag.find('p').text)


print(msgs_last_collect)

ultima = soup.find_all(class_="last-service")

ultima_coleta_datas = []
for data in ultima:
    texto = data.get_text(strip=True)
    if "Last collection" in texto:
        texto = texto.replace("Last collection", "").strip()
    if texto:
        ultima_coleta_datas.append(texto)

# print(ultima_coleta_datas)


proxima = soup.find_all(class_="next-service")

proxima_coleta_datas = []
for data in proxima:
    texto = data.get_text(strip=True)
    if "Next collection" in texto:
        texto = texto.replace("Next collection", "").strip()
    if texto:
        proxima_coleta_datas.append(texto)

# print(proxima_coleta_datas)

final = []

for c in range(2):
    temp = [ultima_coleta_datas[c],msgs_last_collect[c],proxima_coleta_datas[c]]
    final.append(temp)    

print(final)