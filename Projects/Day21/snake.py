from turtle import Turtle
from random_color import create_random_color

# constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {"Up": 90, "Down": 270, "Left": 180, "Right": 0}


class Snake:

    def __init__(self):
        self.all_snake_parts = []
        self.create_snake()
        self.head = self.all_snake_parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_part(position)

    def add_snake_part(self, position):
        new_snake_part = Turtle(shape="square")
        new_snake_part.color(create_random_color())
        new_snake_part.penup()
        new_snake_part.goto(position)
        self.all_snake_parts.append(new_snake_part)

    def extend_snake(self):
        self.add_snake_part(self.all_snake_parts[-1].position())

    def move(self):

        for snake_part_num in range(len(self.all_snake_parts) - 1, 0, -1):
            new_x = self.all_snake_parts[snake_part_num - 1].xcor()
            new_y = self.all_snake_parts[snake_part_num - 1].ycor()
            self.all_snake_parts[snake_part_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTIONS['Down']:
            self.head.setheading(DIRECTIONS['Up'])

    def down(self):
        if self.head.heading() != DIRECTIONS['Up']:
            self.head.setheading(DIRECTIONS['Down'])

    def left(self):
        if self.head.heading() != DIRECTIONS['Right']:
            self.head.setheading(DIRECTIONS['Left'])

    def right(self):
        if self.head.heading() != DIRECTIONS['Left']:
            self.head.setheading(DIRECTIONS['Right'])
