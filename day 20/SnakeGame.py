from turtle import Turtle, Screen
import time

        

class SnakeGame:
    screen = Screen()
    screen.tracer(0)
    screen.tracer(0)


    screen.title("Snake Game") 
    screen.setup(width=1000, height=600)
    screen.bgcolor("black")

    pos = [(0,0), (-20,0), (-40,0)]
    corpo = []

    for c in pos:
        temp = Turtle()
        temp.color("green")
        
        temp.shape("square")
        temp.penup()
        temp.goto(c)
        corpo.append(temp)

        
    screen.update()

    while True:
        for c in corpo:
            c.forward(20)
            time.sleep(0.1)
        screen.update()



    screen.exitonclick()
        
    
        