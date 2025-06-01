from turtle import Turtle,Screen


class Paddle(Turtle):
    def __init__(self,x_cordinate):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.shapesize(5,1)
        self.penup()
        self.setx(x_cordinate)



    def go_up(self):
        # new_y= self..ycor()+20
        if self.ycor() < 220:
            self.goto(self.xcor(),self.ycor()+20)
        else:
            pass

    def go_down(self):
        if self.ycor() > -220:
            self.goto( self.xcor(), self.ycor()-20)
        else:
            pass





