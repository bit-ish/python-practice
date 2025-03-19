
import turtle as t
import random

sandy=t.Turtle()
my_screen=t.Screen()

sandy.shape("turtle")
sandy.color("blue","white")


colors=["blue","red","yellow","pink","black","cyan","magenta","green","orange"]
sides=3

while sides<13:
    sandy.color(random.choice(colors))

    for a in range(sides):
        # sandy.color(random.choice(colors))
        sandy.fd(50)
        sandy.left(360/sides)
    sides+=1





my_screen.exitonclick()

>>>>>>>