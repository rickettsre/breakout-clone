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
screen.setup(800, 600)  # Width Height x 380 to -380 y 280 to -280
screen.setup()
screen.title("Breakout")
screen.tracer(0)  # screen tracer

scoreboard = Scoreboard(y_position=0)
paddle = Paddle()
court = Court()
ball = Ball()

brick = Bricks()
# Ideally 14 bricks
brick.create_bricks("yellow", -300, 125)
brick.create_bricks("yellow", -200, 150)
brick.create_bricks("green", -100, 175)
brick.create_bricks("green", 0, 200)
brick.create_bricks("orange", 100, 225)
brick.create_bricks("orange", 200, 250)
brick.create_bricks("red", 300, 275)
brick.create_bricks("red", 400, 300)

screen.listen()

screen.onkeypress(key="Left", fun=paddle.move_left)
screen.onkeypress(key="Right", fun=paddle.move_right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)  # increase the ball speed after each bounce
    ball.move()
    # print(ball.xcor(), ball.ycor())
    # print(f"Ball Distance: {ball.distance(paddle)}")

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
    #  scoreboard.increase_score()

    # Brick collision
    for obj in brick.bricks:
        if ball.distance(obj) < 20:
            print("Hit Brick")
            brick.remove_brick(obj)

        # print(ball.distance(obj))
    # print(brick.bricks)

    # for brick in brick.bricks:
    #     print(brick.xcor())

    # for brick in brick.bricks:
    #     if ball.distance(brick) < 50:
    #         print("Hit Brick")
#     print(brick.xcor())


screen.exitonclick()
