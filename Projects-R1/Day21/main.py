from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WALLS = {"LEFT": -290, "RIGHT": 290, "TOP": 290, "BOTTOM": -290}

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.colormode(255)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

print(f"Initial cord_x= {snake.head.xcor()} , cord_y= {snake.head.ycor()}")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # detect collision with walls
    if snake.head.xcor() > WALLS["RIGHT"] or snake.head.xcor() < WALLS["LEFT"] or snake.head.ycor() > WALLS["TOP"] \
            or snake.head.ycor() < WALLS["BOTTOM"]:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail without head
    for snake_part in snake.all_snake_parts[1:]:
        if snake.head.distance(snake_part) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
