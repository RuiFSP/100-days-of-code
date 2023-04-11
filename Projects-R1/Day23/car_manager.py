from turtle import Turtle
import random
from random_color import create_random_color

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.create_car()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    # create random cars in y_axis
    def create_car(self):
        random_change = random.randint(1, 6)
        if random_change == 1:
            new_car = Turtle(shape="square")
            new_car.color(create_random_color())
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(x=300, y=random.randint(-250, 250))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    # refresh position of cars
    def refresh_car_position(self):
        for car_num in self.all_cars:
            car_num.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT




