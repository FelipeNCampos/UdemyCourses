from turtle import Screen
import time 

from .Snake import Snake

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from day_21.Food import Food 
from day_21.ScoreBoard import ScoreBoard 

class Game:

    def __init__(self):
        cobra = Snake()
        screen = Screen()
        Score = ScoreBoard()

        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("Snake Game")
        screen.tracer(0)
        screen.listen()
        screen.onkey(cobra.up, "Up")
        screen.onkey(cobra.down, "Down")
        screen.onkey(cobra.left, "Left")
        screen.onkey(cobra.right, "Right")
        food = Food()

        gamon =  True
        while gamon:
            cobra.move()
            screen.update() 
            time.sleep(0.1)
            if cobra.corpo[0].xcor() > 290 or cobra.corpo[0].xcor() < -290 or cobra.corpo[0].ycor() > 290 or cobra.corpo[0].ycor() < -290:
                gamon = False
                print("Game Over")
                screen.clear()

            if cobra.corpo[0].distance(food) < 15:
                food.refresh()
                cobra.add_segment()
                cobra.score += 1
                Score.increase_score()

            if cobra.colision():
                gamon = False
                print("Game Over")
                screen.clear()
                Score.update_scoreboard()
        screen.exitonclick()

