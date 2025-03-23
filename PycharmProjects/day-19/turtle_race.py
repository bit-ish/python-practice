from turtle import Turtle, Screen

import random

game_on =False
my_screen=Screen()

turtles=[]

my_screen.setup(width=500,height=500)

user_bet=my_screen.textinput(title="make a bet",prompt="pick a color")

colors=["red","blue","yellow","violet","indigo","green","orange"]


game_on=True



for turtle in range(0,7):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-225, y=(3 - turtle) * 50)
    new_turtle.color(colors[turtle])
    turtles.append(new_turtle)

while game_on:

    for timmys in turtles:


        timmys.forward(random.randint(10, 20))

        if timmys.xcor()>200:
            game_on=False
            winner=timmys.pencolor()

            if user_bet==winner:

                print(f"you have won! the winner is {winner}")
            else:

                print(f"you have lost! the winner is {winner}")

my_screen.exitonclick()