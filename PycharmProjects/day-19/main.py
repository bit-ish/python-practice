from turtle import Turtle,Screen


timmy=Turtle()
my_screen=Screen()

def move():
    timmy.fd(20)


# using event listeners to take input from keyboard on the screen
# using function as argument in another function
my_screen.onkey(move,"space")

my_screen.listen()

my_screen.exitonclick()
