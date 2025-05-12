from turtle import Turtle,Screen
import time
from snake import Snake

my_screen=Screen()
my_screen.screensize(600,600,"black")
my_screen.title("My Stupid Snake")
my_screen.tracer(0)

starting_pos=[]

saanp=Snake()

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



my_screen.exitonclick()