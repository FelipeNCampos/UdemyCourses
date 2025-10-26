from bs4 import BeautifulSoup
import requests


content = requests.get("https://environmentservices.camden.gov.uk/property/5035135")

html = content.text

soup = BeautifulSoup(html, 'html.parser')


msgs = soup.find_all(class_="task-state")


msgs_last_collect = []

for tag in msgs:
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

proxima = soup.find_all(class_="next-service")

proxima_coleta_datas = []
for data in proxima:
    texto = data.get_text(strip=True)
    if "Next collection" in texto:
        texto = texto.replace("Next collection", "").strip()
    if texto:
        proxima_coleta_datas.append(texto)

final = []

for c in range(2):
    temp = [ultima_coleta_datas[c],proxima_coleta_datas[c]]
    final.append(temp)    

print(final)