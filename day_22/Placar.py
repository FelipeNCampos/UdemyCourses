from turtle import Turtle



class Placar(Turtle):
    score_left = 0
    score_right = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score_left} : {self.score_right}", align="center", font=("Courier", 24, "normal"))
        
    def left_point(self):
        self.score_left += 1
        self.update_scoreboard()

    def right_point(self):
        self.score_right += 1
        self.update_scoreboard()

