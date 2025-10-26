from bs4 import BeautifulSoup
import requests

print("Iniciando request dos filmes")
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

if response.status_code==200:
    print("Request dos filmes concluido com sucesso")
else:
    raise Exception(f"Erro ao fazer request dos filmes code {response.status_code}")


