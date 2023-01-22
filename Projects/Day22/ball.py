from turtle import Turtle
from random_color import create_random_color


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color(create_random_color())
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= - 1
        self.move_speed *= 0.8

    def bounce_x(self):
        self.x_move *= - 1
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
