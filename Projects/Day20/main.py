from turtle import Screen
from snake import Snake
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.colormode(255)
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_oon = True
while game_is_oon:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
