from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PING PONG")

paddle_right = Paddle(380)
paddle_left = Paddle(-380)
ball = Ball()

b_top = 280.00
b_bottom = -280.00
b_right = 360
b_left = -360

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

moving = True
while moving:

    # detect collision with the wall
    if ball.ycor() > b_top or ball.ycor() < b_bottom:
        ball.bounce()

    # detect collision with the paddle
    if ball.xcor() > b_right or ball.xcor() < b_left:
        if ball.distance(paddle_right) < 40:
            ball.dx *= -1
        elif ball.distance(paddle_left) < 40:
            ball.dx *= -1
        else:
            # detect r paddle misses
            if ball.xcor() == 380:
                scoreboard.l_point()
                ball.reset()
            # detect l paddle misses
            if ball.xcor() == -380:
                scoreboard.r_point()
                ball.reset()

    screen.update()
    time.sleep(0.1)
    ball.move()

screen.exitonclick()
