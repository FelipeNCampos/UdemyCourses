from turtle import Turtle
import time
import random

class Bola(Turtle):
    xvelocidade = 0
    yvelocidade = 0

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed(2)

    def reset(self):
        for c in range(3):
            self.hideturtle()
            time.sleep(0.1)
            self.showturtle()

        self.speed(0)
        self.goto(0, 0)
        self.speed(1.5)


        time.sleep(1)
        self.start()

    
    def start(self):
        lado = random.choice([-1, 1])

        self.xvelocidade = random.randint(5, 10)*lado
        self.yvelocidade = random.randint(5, 10)*lado

        self.goto(0, 0)
        self.setheading(0)


    def move(self):
        new_x = self.xcor() + self.xvelocidade
        new_y = self.ycor() + self.yvelocidade

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.yvelocidade *= -1
        self.xvelocidade *= 1.2	
        self.yvelocidade *= 1.2


    def bounce_x(self):
        self.xvelocidade *= -1
        self.xvelocidade *= 1.2
        self.yvelocidade *= 1.2
    

