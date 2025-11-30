from bs4 import BeautifulSoup
import requests as re

try : 
    tempo = input("Digite a data em que quer voltar : (O formato deve ser dd-mm-yyyy) : \n")
    
except Exception as e:
    print("Erro ao coletar data de busca do usuario")
