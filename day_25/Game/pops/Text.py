from turtle import Turtle 



class Text(Turtle):


    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.hideturtle()


    def write(self, texto, x, y):
        self.goto(x,y)
        return super().write(texto, move=False)