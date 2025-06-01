from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()

screen.screensize(800,500,"black")
screen.title("MY BONG GAME ")
screen.tracer(0)

paddle_R=Paddle(350)
paddle_L=Paddle(-350)
ball = Ball()
scoreboard=Scoreboard()

screen.listen()

screen.onkey(paddle_R.go_up,"Up")
screen.onkey(paddle_R.go_down ,"Down")
screen.onkey(paddle_L.go_up,"w")
screen.onkey(paddle_L.go_down,"s")



game_on=True

# a=0
while game_on:
    time.sleep(ball.speeed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() <- 280 :
         ball.v_bounce()

    if ball.xcor()> 330 and ball.distance(paddle_R) < 55 or ball.xcor()< -330 and ball.distance(paddle_L) < 55 :
        ball.h_bounce()
        ball.speeed*= 0.9

    if ball.xcor()> 360:

        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -360:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()