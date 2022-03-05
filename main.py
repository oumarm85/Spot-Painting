#import colorgram
# colors = colorgram.extract('spots.jpeg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     the_color = (r, g, b)
#     rgb_colors.append(the_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random

color_list =[(141, 163, 182), (14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62), (220, 156, 97), (150, 17, 34), (122, 72, 100), (13, 143, 53), (74, 29, 35), (59, 34, 31), (204, 67, 26), (226, 170, 199), (242, 80, 27), (16, 172, 189), (34, 176, 93), (2, 114, 63), (247, 214, 2), (114, 188, 142), (181, 95, 111), (188, 182, 211), (40, 39, 46), (157, 207, 217), (229, 173, 162), (162, 208, 181), (118, 117, 163)]

colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed(0)
tim.sety(-200)

for _ in range(10):
    tim.setx(-200)
    tim.sety(tim.ycor() + 50)
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.setx(tim.xcor() + 50)

screen = Screen()
screen.exitonclick()