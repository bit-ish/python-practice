import time
from turtle import Screen, Turtle
from turtledemo.penrose import start

screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title(" My Snake Game ! ")
screen.tracer(0)



positions=[(0,0),(-20,0),(-40,0)]

segments=[]

for _ in positions:
    new_segment=Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(_)
    segments.append(new_segment)

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.fd(20)
    for seg_num in range(len(segments)-1 ,0,-1):
        new_x= segments[seg_num-1].xcor()
        new_y= segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)

    segments[0].fd(20)













screen.exitonclick()