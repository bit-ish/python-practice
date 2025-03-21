import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
my_screen=Screen()

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    colors=(r,g,b)
    return colors

x=random.randint(0,4)

buns=Turtle()
buns.speed("fastest")
buns.pensize(2)
buns.shape="turtle"
# buns.color(random_color())

# for a in range(100):
#     x = random.randint(0, 4)
#     buns.color(random_color())
#
#     buns.color()
#     buns.fd(20)
#     buns.setheading(90*x)
#     print(90*x)

# heading=0

def spirograph(gap):
    for b in range(int(360/gap)):
        buns.color(random_color())
        buns.seth(buns.heading()+gap)

        buns.circle(100)


spirograph(15)

my_screen.exitonclick()