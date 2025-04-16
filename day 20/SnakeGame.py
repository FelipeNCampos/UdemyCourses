from turtle import Turtle, Screen

class Quadrado(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(x, y)

class SnakeGame:
    screen = Screen()
    
    corpo = []
    for c in range(3):
        x = c * 20
        corpo.append(Quadrado(x, 0))

    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")


        

        self.screen.setup(width=600, height=600)     
        self.screen.exitonclick()   






play = SnakeGame()

