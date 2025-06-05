from turtle import Turtle
import time
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
# SLEEP=0.9/

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()

        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
        # time.sleep(0.9)

