from turtle import Screen, Turtle
import pandas as pd 
import time 
from pops.Score import Score

class Game:

    def __init__(self):
        self.text = Turtle()
        self.alerta = Turtle()
        self.screen = Screen()
        self.score = Score()

        content = pd.read_csv("50_states.csv")

        states = content["state"].values

        self.screen.bgpic("blank_states_img.gif")
        self.screen.setup(745,491)
        self.text.hideturtle()
        self.alerta.hideturtle()

        print(states)
        print (content)

        
        onoff = 1
        self.resp = []
        while onoff:
            temp  = self.screen.textinput("Hey","Guess a state :")

            if (temp in self.resp):
                self.alerta.hideturtle()
                self.alerta.penup()
                self.alerta.goto(0,0)
                self.alerta.write("Resposta repetida", align="center", font=("Arial", 24, "normal"))
                self.alerta.getscreen().ontimer(self.alerta.clear, 2000)
                time.sleep(2)

            if temp in states and temp not in self.resp:
                self.text.penup()
                self.text.hideturtle()
                self.resp.append(temp)

                row = content[content['state'] == temp]
                x,y = int(row["x"].iloc[0]),int(row["y"].iloc[0])

                self.text.goto(x,y)

                self.text.write(temp,move=True,align="left")
                self.score.increase_score()

                
            if (temp not in states):
                onoff = 0

        self.screen.mainloop()




play = Game()