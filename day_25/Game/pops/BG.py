from turtle import Turtle


class BG(Turtle):


    def __init__(self,bg):
        super().__init__()

        self.shape(bg)
        self.penup()

        
        self.goto(0, -50)  
        self.showturtle()  

