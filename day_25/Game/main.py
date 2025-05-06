import pandas as pd 
from turtle import Screen
from pops.Score import Score
from pops.BG import BG
from pathlib import Path
from pops.Text import Text

class Game:

    def __init__(self):
        dir_script = Path(__file__).parent.resolve()
        self.bggif = str(dir_script / 'data' / 'bg.gif')
        self.statespath = str(dir_script / 'data' / 'states.csv')
        
        self.screen  = Screen()
        self.score =  Score()
        self.texto = Text()

        self.screen.addshape(self.bggif)
        self.bg = BG(self.bggif)
        self.screen.title("guess 50 U.S. states")

        self.play()
        
        self.screen.exitonclick()

    def play(self):
        content = pd.read_csv(self.statespath)
        states = content["state"].tolist()

        print(states)
        print(content)

        onoff = True
        resp  = []
        while onoff:
            temp = self.guess()

            if temp not in states or temp in resp:
                self.score.endRun()
                onoff = False
                
            if temp in states and temp not in resp:
                row = content[content['state'] == temp]
                x,y = int(row['x'].iloc[0]-40),int(row['y'].iloc[0]-70)
                self.texto.write(temp,x,y)
                resp.append(temp)
                self.score.incressScore()

                


    def guess(self):
        temp = self.screen.textinput("title","guess:")
        return str(temp)

start = Game()