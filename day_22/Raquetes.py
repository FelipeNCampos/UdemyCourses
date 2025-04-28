from turtle import Turtle 


class Raquete(Turtle):
    def __init__(self, posicao):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.goto(posicao)