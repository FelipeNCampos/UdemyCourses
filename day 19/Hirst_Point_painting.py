import turtle as t
import random as r
import colorgram as cl

def get_colors(img, num_colors):
    processed = []

    resul = cl.extract(img,num_colors)
    for c in resul:
        r = c.rgb.r
        g = c.rgb.g
        b = c.rgb.b
        processed.append((r,g,b))
    return processed


tim = t.Turtle()
t.colormode(255)
colors = get_colors("painting.jpeg",10)
tim.penup()

tim.goto(-100,-100)

def paint_line():
    tim.color(r.choice(colors))
    tim.dot(10)
    for c in range(4):
        tim.forward(50)
        tim.dot(10)
        tim.color(r.choice(colors))
    tim.left(90)
    tim.forward(50)
    tim.left(90)

    tim.color(r.choice(colors))
    tim.dot(10)
    for c in range(4):
        tim.forward(50)
        tim.dot(10)
        tim.color(r.choice(colors))

    tim.right(90)
    tim.forward(50)
    tim.right(90)





for c in range(3):
    paint_line()




tim.color("white")
tela = t.Screen()
tela.exitonclick()

