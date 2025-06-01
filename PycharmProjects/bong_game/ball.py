from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speeed=0.1

        # self.shapesize(.5)
        self.color("white")
        self.x_move=10
        self.y_move=10


    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
        self.speed(self.speed())

    def v_bounce(self):
        self.y_move *=- 1

    def h_bounce(self):
        self.x_move *=- 1
        self.speeed *=0.9
    def reset(self):
        self.speeed= 0.1
        self.home()
        self.h_bounce()

    # def speed_up(self):
    #     self.speeed += 5
    #     self.speed(self.speed())


