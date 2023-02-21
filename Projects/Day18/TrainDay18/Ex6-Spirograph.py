from turtle import Screen
from random import randint
import turtle as t

rotation = [0, 90, 180, 270]

screen = Screen()
screen.colormode(255)  # needed to use rgb
t.speed(0)


def my_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_color = (r, g, b)

    return rand_color


def draw_spirograph(angle_to_shift):
    for _ in range(int(360 / angle_to_shift)):
        t.pencolor(my_random_color())
        t.circle(100)
        t.left(angle_to_shift)


draw_spirograph(5)

screen.exitonclick()
