import json 
import os


class Util:

    @staticmethod
    def getDictWords():
        with open('data/words.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    

    @staticmethod
    def addPalavraConhecida(word):
        try:
            with open("data/know.json","r") as file:
                print("Arquivo de palavras conhecidas encontrado, prosseguindo com adição de palavra conhecida")

        except FileNotFoundError:    
            print("Arquivo de palavras conhecidas não encontrado, prosseguindo para criação:")
            os.makedirs(os.path.dirname("data/knwo.json"), exist_ok=True)
            with open("data/know.json", "w") as file:
                json.dump([], file, indent=4)
        
        with open("data/know.json", "r") as f:
            dataDict = json.load(f)
        
        dataDict.append(word)
        
        with open("data/know.json", "w") as f:
            json.dump(dataDict, f, indent=4)


    @staticmethod
    def readKnow():
        try:
            with open("data/know.json","r") as f:
                return json.load(f)
        except:
            return ""