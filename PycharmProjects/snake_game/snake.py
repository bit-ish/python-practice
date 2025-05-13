from turtle import Turtle,Screen

MOVE=20
''' constants are written in upper case. '''
STARTING_POSTION=[(-20,0),(-40,0),(-60,0)]

UP=90
DOWN=270
LEFT=180
RIGHT=  0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        '''⬆️This will be executed whenever Snake class is used '''
        self.head=self.segments[0]

    # def create_snake(self):
    #     for num in range(0, 10):
    #         self.add_segment()
    def create_snake(self):
        for position in STARTING_POSTION:
            self.add_segment(position)


    def add_segment(self,position):
        turtly = Turtle("square")
        turtly.color("white")
        turtly.penup()
        turtly.goto(position)
        self.segments.append(turtly)

    def extend(self):
        self.add_segment(self.segments[-1].position())



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



