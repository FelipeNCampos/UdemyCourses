from turtle import Turtle 



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90) 
        self.penup()
        self.speed(0)
        self.goto(0,-240)


    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < 280: 
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > -240: 
            self.goto(self.xcor(), new_y)