from bs4 import BeautifulSoup
import requests

print("Iniciando request dos filmes")
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

if response.status_code==200:
    print("✓ Request dos filmes concluido com sucesso")
else:
    raise Exception(f"Erro ao fazer request dos filmes code {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
arquivo = "movies.txt"

print(f"iniciando a escrita dos filmes no arquivo {arquivo}")
try:
    with open(arquivo, 'w', encoding='utf-8') as file :
        proc = soup.find_all(class_="gallery__content-item gallery__content-item--gallery")
        for filme in reversed(proc[:100]):
            titulo = filme.find(class_="title").text
            print(titulo)
            file.write(f"{titulo}\n")
        ultimo = soup.find_all(class_="gallery__content-item gallery__content-item--gallery gallery__content-item--primary")[0].find(class_="title").text
        print(f"{ultimo}")
        file.write(ultimo)
    print(f"Sua lista dos 100 melhores filmes de todos os tempos esta disponivel para consulta no arquivo {arquivo}")
    
except Exception as e:
    print(f"Algo deu errado com a escrita dos filmes no arquivo {arquivo} : {e}")