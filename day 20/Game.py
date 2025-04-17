from turtle import Screen
import time 

from Snake import Snake

class Game:
    cobra = Snake()
    
    def __init__(self):
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("Snake Game")
        screen.tracer(0)
        screen.listen()
        screen.onkey(self.cobra.up, "Up")
        screen.onkey(self.cobra.down, "Down")
        screen.onkey(self.cobra.left, "Left")
        screen.onkey(self.cobra.right, "Right")

        gamon =  True
        while gamon:
            self.cobra.move()
            screen.update() 
            time.sleep(0.1)
            if self.cobra.corpo[0].xcor() > 290 or self.cobra.corpo[0].xcor() < -290 or self.cobra.corpo[0].ycor() > 290 or self.cobra.corpo[0].ycor() < -290:
                gamon = False
                print("Game Over")
                screen.clear()

        screen.exitonclick()

play = Game()