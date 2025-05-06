from turtle import Turtle 
from pathlib import Path


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,250)


        dir_script = Path(__file__).parent.resolve()
        self.arquivo_path = dir_script / 'hs.txt'

        self.score  = 0
        self.hs = int(self.readHS())

        self.updateScore()

    
    def readHS(self):


        if not self.arquivo_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.arquivo_path}")

        try:
            with self.arquivo_path.open('r', encoding='utf-8') as f:
                conteudo = f.read()
            print(f"leitura do hs : {conteudo}")
            return conteudo
        except IOError as e:
            print(f"Erro ao ler arquivo: {e}")

    def saveHS(self,score = 0):
        with self.arquivo_path.open('w', encoding="utf-8") as f:
            f.write(str(score))


    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score}/50 | High Score: {self.hs}/50", align="center", font=("Courier", 24, "normal"))

    def incressScore(self):
        self.score += 1
        self.updateScore()

    def endRun(self):
        if (self.score > self.hs):
            self.saveHS(self.score)
            self.readHS()
            self.score = 0
            self.updateScore()




