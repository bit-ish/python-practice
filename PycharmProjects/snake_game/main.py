from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen=Screen()
my_screen.screensize(600,600,"black")
my_screen.title("My Stupid Snake")
my_screen.tracer(0)

starting_pos=[]

saanp=Snake()
food=Food()
scoreboard=Scoreboard()

my_screen.listen()
my_screen.onkey(saanp.up,"Up")
my_screen.onkey(saanp.down,"Down")
my_screen.onkey(saanp.left,"Left")
my_screen.onkey(saanp.right,"Right")


game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    saanp.move()

    # Detects collision with food
    if saanp.head.distance(food) < 25:
        print("nom nom!")
        food.refresh()
        scoreboard.increase_score()
        saanp.extend()

    # detects collision with food
    if saanp.head.xcor() > 359 or saanp.head.xcor() < -350 or saanp.head.ycor() < -350 or saanp.head.ycor() < -350:
        game_is_on=False
        scoreboard.game_over()

    # Detecting collision with it's tail
    for seg in saanp.segments[1: ]:
        # if saanp.head==seg:
        #     pass
        # el
        if saanp.head.distance(seg)<10:
            game_is_on = False
            scoreboard.game_over()

my_screen.exitonclick()