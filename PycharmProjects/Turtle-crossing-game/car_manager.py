from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance=random.randint(1,7)
        if random_chance==4:
            new_turtle=Turtle()
            new_turtle.shape("square")
            new_turtle.shapesize(1, 2)
            new_turtle.penup()
            new_turtle.goto(270, random.randint(-250, 250))
            new_turtle.setheading(180)
            new_turtle.color(random.choice(COLORS))
            self.all_cars.append(new_turtle)


    def move(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def speed_up(self):
        self.car_speed+=MOVE_INCREMENT
        self.move()
