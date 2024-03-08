from turtle import Turtle

MOVE_DISTANCE = 20
MAX_SPEED = 0.4


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        if self.move_speed > MAX_SPEED:
            self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        if self.move_speed > MAX_SPEED:
            self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
