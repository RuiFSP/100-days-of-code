from turtle import Turtle, Screen

turtle = Turtle()

for i in range(15):
    turtle.fd(10)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()
