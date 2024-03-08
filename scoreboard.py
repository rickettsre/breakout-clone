from turtle import Turtle

STYLE = ("Impact", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self, y_position=0):
        super().__init__()
        self.score = 0
        self.color("#cccccc")
        self.penup()
        self.hideturtle()
        self.goto(y_position, 350)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", font=STYLE, align="center")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
