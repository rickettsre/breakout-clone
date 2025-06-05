from turtle import Turtle


class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.num_bricks = 17
        self.bricks = []

    def create_bricks(self, color: str, x_position: int, y_position: int, points: int):
        x_position = -400
        for brick in range(self.num_bricks):
            brick = Turtle()
            brick.shapesize(stretch_len=2, stretch_wid=0.5)
            brick.color(color)
            brick.point = points
            brick.shape("square")
            brick.penup()
            brick.goto(x_position, y_position)
            self.bricks.append(brick)
            x_position += 50

    def remove_brick(self, obj):
        obj.hideturtle()  # hide the brick
        self.bricks.remove(obj)  # remove from list

    def reset_bricks(self):
        for brick in self.bricks:
            brick.hideturtle()
        self.bricks.clear()  # clear the list of bricks
