from turtle import Turtle, Screen
import time

        

class SnakeGame:
    screen = Screen()
    screen.tracer(0)


    screen.title("Snake Game") 
    screen.setup(width=1000, height=600)
    screen.bgcolor("black")

    pos = [(0,0), (-20,0), (-40,0)]
    corpo = []
    def __init__(self):
            
        for c in self.pos:
            temp = Turtle()
            temp.color("green")
            
            temp.shape("square")
            temp.penup()
            temp.goto(c)
            self.corpo.append(temp)

            
        self.screen.update()

        flag = 1

        self.screen.listen()
        while flag:
            for c in range(len(self.corpo)-1, 0, -1):
                x = self.corpo[c-1].xcor()
                y = self.corpo[c-1].ycor()
                self.corpo[c].goto(x,y)
            

            self.corpo[0].forward(20)
            
            self.screen.update()
            
            if self.corpo[0].xcor() > 500 or self.corpo[0].xcor() < -500 or self.corpo[0].ycor() > 300 or self.corpo[0].ycor() < -300:
                flag = 0
                print("Game Over")

            time.sleep(0.1)

        self.screen.exitonclick()


game = SnakeGame()
        
    
        