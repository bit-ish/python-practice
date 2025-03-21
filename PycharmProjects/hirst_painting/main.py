# import colorgram
#
# colors=colorgram.extract('hirst_spot.jpg',60)
# rgb_colors=[]
#
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#
#     new_color=(r,g,b)
#
#     rgb_colors.append(new_color)
#
#
#
# print(rgb_colors)
import random
import turtle
from turtle import Turtle,Screen
turtle.colormode(255)

color_list=[(211, 151, 119), (122, 171, 209), (210, 135, 158), (230, 223, 113), (178, 10, 36), (165, 85, 44), (29, 101, 174), (213, 76, 105), (151, 60, 90), (134, 183, 148), (237, 164, 184), (236, 168, 160), (20, 48, 144), (67, 21, 7), (124, 228, 196), (222, 79, 53), (39, 184, 141), (158, 18, 13), (172, 147, 41), (11, 22, 83), (169, 185, 230), (76, 13, 30), (95, 116, 188), (55, 127, 85), (33, 165, 199), (15, 106, 53), (127, 214, 232), (18, 52, 33), (237, 236, 1), (98, 86, 12), (255, 1, 46)]

pichu=Turtle()
pichu.shape("turtle")

# pichu.stamp()
pichu.speed(0)
pichu.penup()
pichu.setheading(225)
pichu.fd(400)
pichu.setheading(0)

for a in range(10):
    for _ in range(10):
        pichu.dot(25,random.choice(color_list))
        pichu.fd(60)
    pichu.teleport(pichu.xcor()-600,pichu.ycor()+65)

pichu.ht()

my_screen=Screen()
my_screen.exitonclick()