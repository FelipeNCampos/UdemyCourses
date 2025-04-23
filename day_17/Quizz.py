
from Question import Question
import random 

class Quizz:
    
    questions = []
    total = 0

    def __init__(self):
        for c in range(int(input("Digite quantas perguntas quer cadastrar : "))):
            texto = input(f"Digite o enunciado da {c+1} pergunta : ")
            resp = input(f"Digite a resposta da {c+1} pergunta : ")

            self.questions.append(Question(texto,resp))
            self.total += 1

    def play(self):
        r = True
        
        stk = 0 
        index = 0

        while r :
            n = random.randint(0,self.total-1)
            print(f"\n"*100)
            print(f"Pontuação atual {stk}/{index}\n{f"\n\n-Pergunta numero {index+1}-":^50}")
            temp = input(f"{self.questions[n].enunciado} : ")
            if (self.questions[n].gabarito != temp):
                print(f"{"YOU LOSE":^50}")
                print(f"Pontuação final {stk}/{index+1}")
                r = False
            else:
                stk += 1
            index += 1


solution = Quizz()
solution.play()

