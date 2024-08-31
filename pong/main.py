import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p1_paddle = Paddle(-350, 0)
p2_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(p1_paddle.up, "w")
screen.onkey(p1_paddle.down, "s")
screen.onkey(p2_paddle.up, "Up")
screen.onkey(p2_paddle.down, "Down")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with upper or lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with left paddle or right paddle
    if ball.distance(p2_paddle) < 50 and ball.xcor() > 320 or ball.distance(p1_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect if collision with left or right wall
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.p1_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.p2_point()



screen.exitonclick()