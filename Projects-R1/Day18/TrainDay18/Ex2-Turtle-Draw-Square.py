from turtle import Turtle, Screen

turtle_draw_square = Turtle()


def draw_square():
    for _ in range(4):
        turtle_draw_square.forward(100)
        turtle_draw_square.right(90)


draw_square()

screen = Screen()
screen.exitonclick()
