from turtle import Screen, Turtle
import time


class Snake:
    corpo = []

    def __init__(self):
        start_position = [(0,0), (-20,0), (-40,0)]

        for position in start_position:
            temp = Turtle()
            temp.shape("square")
            temp.color("white")
            temp.penup()
            temp.goto(position)

            self.corpo.append(temp)

    def move(self):
        for index in range(len(self.corpo)-1, 0, -1):
            new_x = self.corpo[index-1].xcor()
            new_y = self.corpo[index-1].ycor()
            self.corpo[index].goto(new_x, new_y)
        self.corpo[0].forward(20)


    def right(self):
        if self.corpo[0].heading() != 180:
            self.corpo[0].setheading(0)

    def up(self):
        if self.corpo[0].heading() != 270:
            self.corpo[0].setheading(90)


    def left(self):
        if self.corpo[0].heading() != 0:
            self.corpo[0].setheading(180)

    def down(self):
        if self.corpo[0].heading() != 90:
            self.corpo[0].setheading(270)



