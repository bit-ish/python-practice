from turtle import Turtle,Screen
import random

my_screen=Screen()
colors=["red", "blue", "green", "yellow", "purple", "orange", "pink", "black", "brown", "gray"]

x=random.randint(0,4)

buns=Turtle()
buns.speed(0)
buns.pensize(10)
buns.shape="turtle"
buns.color("violet","yellow")

for a in range(200):
    x = random.randint(0, 4)
    buns.color(random.choice(colors))

    buns.color()
    buns.fd(20)
    buns.setheading(90*x)
    print(90*x)






my_screen.exitonclick()