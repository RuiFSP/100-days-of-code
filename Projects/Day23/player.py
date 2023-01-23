from turtle import Turtle
from random_color import create_random_color

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(create_random_color())
        self.penup()
        self.reset_position()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish(self):
        return True if self.ycor() > FINISH_LINE_Y else False

    def reset_position(self):
        self.goto(STARTING_POSITION)
