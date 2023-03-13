# import colorgram
#
# colors = colorgram.extract('dot.jpeg', 30)
# first_col = colors[0]
# print(first_col.rgb[0])
import random
# def extract_rgb(folder):
#     new_list = []
#
#     for i in range(len(folder)):
#         col = folder[i]
#         r = col.rgb[0]
#         g = col.rgb[1]
#         b = col.rgb[2]
#         new_tuple = (r, g, b)
#         new_list.append(new_tuple)
#
#     return new_list

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


tim.pensize(10)
tim.pencolor('white')
tim.hideturtle()
screen.colormode(255)
color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]

y = 0.00
for i in range(10):
    for j in range(10):
        col = random.choice(color_list)
        tim.dot(20, col)
        tim.penup()
        tim.forward(50)
    y += 50.00
    print(y)
    tim.goto(0.00, y)








screen.exitonclick()




