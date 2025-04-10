from turtle import Turtle, Screen
import random as r


screen = Screen()
screen.title("Turtle race")
cor = screen.textinput("Choise color","Please, text your color : ")

timmy = Turtle()
timmy.color(cor)


t1 = Turtle()
t1.color("blue")

t2 = Turtle()
t2.color("green")

t3 = Turtle()
t3.color("purple")

t4 = Turtle()
t4.color("pink")

raccers = [timmy,t1,t2,t3,t4]

def start():
    for c in raccers:
        c.shape("turtle")
        c.penup()

    timmy.goto(-300,160)
    t1.goto(-300,80)
    t2.goto(-300,0)
    t3.goto(-300,-80)
    t4.goto(-300,-160)


    f = 0
    while not f:
        for c in raccers:
            c.forward(r.randint(1,10))
            if (c.xcor() >=300 ):
                f = raccers.index(c)

    raccers[f].goto(0,0)
    raccers[f].left(60)
    while True:
        raccers[f].left(60)
        raccers[f].right(60)


    






start()
screen.exitonclick()




