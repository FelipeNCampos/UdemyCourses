from Placar import Placar
from turtle import Screen
from Bola import Bola
import time 
from LPlayer import LPlayer
from RPlayer import RPlayer

class Game:
    def __init__(self):
        self.screen = Screen()
        placar = Placar()
        bola = Bola()
        lplayer = LPlayer()
        rplayer = RPlayer()

        self.screen.title("Pong")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        time.sleep(1)
        bola.start()
        
        while 1:
            bola.move()
            if bola.ycor() > 280 or bola.ycor() < -280:
                bola.bounce_y()

            if bola.xcor() > 380:
                placar.left_point()
                bola.reset()

            if bola.xcor() < -380:
                placar.right_point()
                bola.reset()
            if bola.distance(rplayer) < 50 and bola.xcor() > 320:
                bola.bounce_x()
            if bola.distance(lplayer) < 50 and bola.xcor() < -320:
                bola.bounce_x()
            if lplayer.ycor() > 250:
                lplayer.goto(-350, 250)
            if lplayer.ycor() < -240:
                lplayer.goto(-350, -240)

            if rplayer.ycor() > 250:
                rplayer.goto(350, 250)
            if rplayer.ycor() < -240:
                rplayer.goto(350, -240)

            self.screen.listen()
            self.screen.onkeypress(lplayer.up, "w")
            self.screen.onkeypress(lplayer.down, "s")

            self.screen.onkeypress(rplayer.up, "Up")
            self.screen.onkeypress(rplayer.down, "Down")


            self.screen.update()

        self.screen.mainloop()

