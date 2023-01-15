from turtle import Screen
from pad import Pad
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

r_pad = Pad((350, 0))
l_pad = Pad((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(r_pad.go_up, "Up")
screen.onkeypress(r_pad.go_down, "Down")
screen.onkeypress(l_pad.go_up, "w")
screen.onkeypress(l_pad.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with wall
    if ball.ycor() > 287 or ball.ycor() < -287:
        ball.wall_collision()

    # Collision with pad
    if ball.distance(r_pad) < 50 and ball.xcor() > 327 or ball.distance(l_pad) < 50 and ball.xcor() < -327:
        ball.x_collision()

    # Detect misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
