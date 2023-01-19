import turtle
from turtle import Turtle, Screen
import enum

tim = Turtle()
screen = Screen()


class Choice(enum.Enum):
    UP = "w"
    BACK = "s"
    ROTATE_COUNTER_CLOCKWISE = "a"
    ROTATE_CLOCKWISE = "d"
    CLEAR_AND_RESET = "c"


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    turtle.resetscreen()


screen.listen()
screen.onkey(key=Choice.UP.value, fun=move_forwards)
screen.onkey(key=Choice.BACK.value, fun=move_backwards)
screen.onkey(key=Choice.ROTATE_COUNTER_CLOCKWISE.value, fun=turn_left)
screen.onkey(key=Choice.ROTATE_CLOCKWISE.value, fun=turn_right)
screen.onkey(key=Choice.CLEAR_AND_RESET.value, fun=clear)

screen.exitonclick()
