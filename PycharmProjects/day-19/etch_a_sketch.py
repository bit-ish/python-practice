from turtle import Turtle,Screen


timmy=Turtle()
my_screen=Screen()

timmy.shape("turtle")

def move_fd():
    timmy.fd(20)
def move_bk():
    timmy.bk(20)
def move_left():
    timmy.left(10)
def move_right():
    timmy.right(10)

def clr_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()



my_screen.onkey(move_fd,"w")
my_screen.onkey(move_bk,"s")

my_screen.onkey(move_left,"a")
my_screen.onkey(move_right,"d")

my_screen.onkey(clr_screen,"c")




my_screen.listen()

my_screen.exitonclick()


