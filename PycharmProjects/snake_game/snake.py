from turtle import Turtle,Screen

MOVE=20
''' constants are written in upper case. '''

UP=90
DOWN=270
LEFT=180
RIGHT=  0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for num in range(0, 10):
            turtly = Turtle("square")
            turtly.color("white")
            turtly.penup()
            turtly.goto(x=-num * 20, y=0)
            self.segments.append(turtly)

    def move(self):

            for num1 in range(len(self.segments) - 1, 0, -1):
                x_cor = self.segments[num1 - 1].xcor()
                y_cor = self.segments[num1 - 1].ycor()
                self.segments[num1].goto(x_cor, y_cor)

            self.head .fd(MOVE)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)



