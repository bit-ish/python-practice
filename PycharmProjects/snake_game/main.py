from turtle import Screen, Turtle

screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title(" My Snake Game ! ")



positions=[(0,0),(-10,0),(-30,0)]

for _ in positions:
    timmy=Turtle("square")
    timmy.color("white")
    timmy.goto(_)










screen.exitonclick()