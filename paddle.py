from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=0.5)
        self.color("#006187")
        self.penup()
        self.setheading(LEFT)
        self.goto(0, -260)
      

    def move(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(LEFT)
        if self.xcor() > -400:
            self.move()

    def move_right(self):
        self.setheading(RIGHT)
        if self.xcor() < 400:
            self.move()
        

# class RightPaddle(Paddle):
#     def __init__(self):
#         super().__init__()
#         self.goto(350, 0)

# class LeftPaddle(Paddle):
#     def __init__(self):
#         super().__init__()
#         self.goto(-350, 0)



