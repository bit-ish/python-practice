from turtle import Turtle

FONT=("Courier",20,"normal")
ALIGNMENT="center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score=0
        self.penup()
        self.goto(0,335)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}",move=False,align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",move=False,align=ALIGNMENT,font=FONT)


