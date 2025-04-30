from turtle import Turtle
import random
import time 

class Carro(Turtle):
    _carros = []
    _speed = 20
    _level = 1

    def __init__(self, color, y):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(color)
        self.penup()
        self.speed(0)
        if (Carro._level>3):
            l = random.choice([-1,1])
            self.goto(300*l, y)
            if (l==-1):
                self.setheading(0)
            else:
                self.setheading(180)
        else:
            self.goto(300,y)
            self.setheading(180)

        self.showturtle()	

    @staticmethod
    def create_car():
        while True:
            cores = ["red", "blue", "green", "yellow", "purple"]
            cor = random.choice(cores)
            y = random.randint (-250,250)

            novo = Carro(cor,y)
            
            Carro._carros.append(novo)
            time.sleep(0.5)

    @staticmethod
    def move_cars():
        while True:
            for c in Carro._carros:
                c.forward(Carro._speed)
                if (c.xcor() < -400):
                    c.goto(1000,1000)
                    Carro._carros.remove(c)
            time.sleep(0.1)
