from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.lscore} : {self.rscore}", align="center", font=("Courier", 24, "normal"))

    def left_socre(self):
        self.lscore += 1
        self.update_scoreboard()

    def right_score(self):
        self.rscore += 1
        self.update_scoreboard()