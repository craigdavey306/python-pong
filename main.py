from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle(start_x=360, start_y=0)
l_paddle = Paddle(start_x=-360, start_y=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_up, "W")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(l_paddle.move_down, "S")

game_is_on = True
while game_is_on:
    time.sleep(ball.get_move_speed())
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 20 and ball.xcor() > 340 or ball.distance(l_paddle) < 20 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect if ball goes beyond right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect if ball goes beyond left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()


screen.exitonclick()