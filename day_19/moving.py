from turtle import Turtle, Screen

tim  = Turtle()

screen = Screen()

def move_foward():
    tim.forward(10)

def move_back():
    tim.back(10)

def turn_right():
    tim.setheading(tim.heading()+10)

def turn_left():
    tim.left(5)

def clear():
    tim.home()
    tim.clear()

screen.listen()

screen.onkeypress(key="w", fun=move_foward)
screen.onkeypress(key="s", fun=move_back)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()