from turtle import Turtle
import time
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250,270)
        self.score=0
        self.current_score()

    def current_score(self):
        self.write(f"score:{self.score}",False,"left",FONT)

    def update_score(self):
        self.clear()
        self.score+=1
        self.current_score()

    def game_over(self):
        self.clear()
        self.home()
        self.write(f"   GAME OVER \n Final Score:{self.score}",True,'center',FONT)




