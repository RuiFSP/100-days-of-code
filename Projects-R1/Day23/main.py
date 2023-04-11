import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Welcome to Turtle Crossing using Turtle Graphics")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.colormode(255)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.refresh_car_position()

    # detect collision with car:
    for car in car_manager.all_cars:
        if car.distance(player) < 28:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing:
    if player.is_at_finish():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
