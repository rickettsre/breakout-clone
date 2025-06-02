from turtle import Turtle

STYLE = ("Impact", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.lives = 3
        self.color("#cccccc")
        self.penup()
        self.hideturtle()
        self.goto(550, 100)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"Score : {self.score}\n Level: {self.level}\n Lives: {self.lives}",
            font=STYLE,
            align="center",
        )

    def increase_score(self, point):
        self.score += point
        self.clear()
        self.update_scoreboard()

    def lose_life(self, life):
        self.lives -= life
        self.clear()
        self.update_scoreboard()
