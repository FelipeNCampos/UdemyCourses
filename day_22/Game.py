from turtle import Screen

from Score import Score


class Game():
    def __init__(self):
        placar = Score()
        tela = Screen()

        tela.title("Pong")
        tela.bgcolor("black")

        tela.setup(width=800, height=600)

        tela.exitonclick()

