#
# Breakout Game
#

from turtle import Screen
from paddle import Paddle
from court import Court
from scoreboard import Scoreboard
from ball import Ball
from bricks import Bricks
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.setup()
screen.title("Breakout")
screen.tracer(0)  # screen tracer

scoreboard = Scoreboard()
paddle = Paddle()
court = Court()
ball = Ball()

brick = Bricks()
brick.create_bricks("yellow", -300, 125, 1)
brick.create_bricks("yellow", -200, 150, 1)
brick.create_bricks("green", -100, 175, 3)
brick.create_bricks("green", 0, 200, 3)
brick.create_bricks("orange", 100, 225, 5)
brick.create_bricks("orange", 200, 250, 5)
brick.create_bricks("red", 300, 275, 7)
brick.create_bricks("red", 400, 300, 7)

screen.listen()

screen.onkeypress(key="Left", fun=paddle.move_left)
screen.onkeypress(key="Right", fun=paddle.move_right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)  # increase the ball speed after each bounce
    ball.move()

    # Wall collision
    if ball.ycor() > 330 or ball.ycor() < -330:  # ball width is 20px
        ball.bounce_y()
    if ball.xcor() > 438 or ball.xcor() < -438:
        ball.bounce_x()
    # Detect Collision paddles:
    if ball.distance(paddle) < 50 and ball.ycor() < -240:
        ball.bounce_y()
    # Detect Ball out of bounds:
    if ball.ycor() <= -280:
        ball.ball_reset()
    # Brick collision
    for obj in brick.bricks:
        if ball.distance(obj) < 20:
            print(obj.color()[0])
            scoreboard.increase_score(obj.point)
            brick.remove_brick(obj)
            ball.bounce_y()


screen.exitonclick()
