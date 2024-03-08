from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

colors = ["yellow"]
y_position = 100

# 300 red row


class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.num_bricks = 17
        self.bricks = []

    def create_bricks(self):
        x_position = -400
        for brick in range(self.num_bricks):
            # print(f"Creating brick {x}")
            brick = Turtle()
            brick.shapesize(stretch_len=2, stretch_wid=0.5)
            brick.color("yellow")
            brick.shape("square")
            brick.penup()
            brick.goto(x_position, y_position)
            self.bricks.append(brick)
            x_position += 50
