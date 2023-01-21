from turtle import Turtle
from random_color import create_random_color
import random


FOOT_TYPES = ["circle", "square", "triangle"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)  # 15x15 circle
        self.color(create_random_color())
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(create_random_color())
        self.shape(random.choice(FOOT_TYPES))
        cord_x = random.randint(-280, 280)
        cord_y = random.randint(-280, 280)
        self.goto(cord_x, cord_y)
