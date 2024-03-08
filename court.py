from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


LENGTH = 900
WIDTH = 600


class Court(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("pink")
        self.pensize(5)
        self.goto(-450, -255)
        # self.goto(-450, 255)
        self.pendown()
        self.court_draw()

    def court_draw(self):
        print("drawing court")
        for _ in range(4):
            # drawing length
            if _ % 2 == 0 and _ != 0:
                print(_)
                self.pendown()
                self.color("pink")
                self.forward(LENGTH)  # Forward turtle by l units
                self.left(90)  # Turn turtle by 90 degree

            # drawing width
            
            elif _ % 2 == 0 and _ == 0:
                self.penup()
                # self.color("grey")
                self.forward(LENGTH)  # Forward turtle by l units
                self.left(90)  # Turn turtle by 90 degree

            else:
                self.pendown()
                self.color("brown")
                self.forward(WIDTH)  # Forward turtle by w units
                self.left(UP)  # Turn turtle by 90 degree

        self.penup()
        self.hideturtle()
