# pip install colorgram.py
import random
import turtle
from turtle import Screen
from random import randint
import turtle as t
import colorgram

# colors
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

screen = Screen()
screen.colormode(255)
t.speed(0)
t.hideturtle()
row_number = 0
y = 0


def reset_row():
    t.penup()
    t.setheading(225)
    t.forward(300)
    t.setheading(0)
    t.pendown()


while row_number < 10:

    reset_row()

    for _ in range(10):
        t.dot(20, random.choice(rgb_colors))
        t.penup()
        t.forward(50)
        t.pendown()

    y += 30
    row_number += 1

    t.penup()
    t.setpos(0, y)
    t.pendown()

screen.exitonclick()
