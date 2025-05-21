import json 
import os


class Util:

    @staticmethod
    def getDictWords():
        with open('./data/words.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    

    @staticmethod
    def addPalavraConhecida():
        try:
            with open("../../data/teste.json","r") as file:
                print("Arquivo de palavras conhecidas ja existe")

        except FileNotFoundError:    
            print("Arquivo de palavras conhecidas não encontrado, prosseguindo para criação:")
            os.makedirs(os.path.dirname("../../data/teste.json"), exist_ok=True)
            with open("../../data/teste.json", "w") as file:
                json.dump([], file, indent=4)