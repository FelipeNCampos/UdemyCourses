import paiseslog
import random

class LessorOHight:

    def __init__(self):
        print("--------------------Bem vindo ao jogo de QUEM TEM MAIS POPULAÇÃO-------------------\n\nEscolha o pais que acaha ter mais população, acumule streakes acertando consecutivamente.")
        self.play()
        
    def pegar(self):
        temp = random.choice(list(paiseslog.paises.keys()))

        return [temp,paiseslog.paises[temp]]
    
    def play(self):

        print(paiseslog.logo)
        p1 = self.pegar()

        f = 0
        sk = 1
        while (f == 0) :
            p2 = self.pegar()
            r = input(f"\n\nEntre \n\n1 - {p1[0].upper()} \n{paiseslog.vs} \n2 - {p2[0].upper()}\n\nEscolha aquele que acha ter a maior população: ")

            if (r=="1"):
                if (p1[1] > p2[1]):
                    print("--------------------Certa resposta--------------------\n")
                    print(f"____________________{sk} STREAK____________________\n")
                    sk += 1
                else:
                    print("\n--------------------Resposta Errada--------------------\n")
                    print(f"finalizou com {sk-1} acertos consecutivos")

                    answer = ""
                    while (answer not in ['s','n']):
                        answer  = input("\n\nJogar mais uma vez? {s ou n}").lower()
                    if (answer == 's'):
                        print("\n"*200)
                        self.play()
                    return 
                
            elif (r=='2'):
                if (p2[1] > p1[1]):
                    print("--------------------Certa resposta--------------------\n")
                    print(F"____________________{sk} STREAK____________________\n")

                    sk += 1
                    p1 = p2
                else:
                    print("\n--------------------Resposta Errada--------------------\n")
                    print(f"finalizou com {sk-1} acertos consecutivos")
                    
                    answer = ""
                    while (answer not in ['s','n']):
                        answer  = input("\n\nJogar mais uma vez? {s ou n}").lower()
                    if (answer == 's'):
                        print("\n"*200)
                        self.play()
                    return 






solution = LessorOHight()