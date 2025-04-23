import random
import turtle as t

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


timmy = t.Turtle()
t.colormode(255)

timmy.speed('fastest')

tc = 90

for c in range(tc):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.right(360/tc)






tela = t.Screen()
tela.exitonclick()