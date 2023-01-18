from turtle import Screen
from random import randint
import turtle as t

angle = 360
my_range = 3
screen = Screen()
screen.colormode(255)

while my_range < 10:

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_color = (r, g, b)

    for _ in range(my_range):

        t.pencolor(rand_color)
        t.right(angle / my_range)
        t.forward(100)

    my_range += 1


screen.exitonclick()