from turtle import Turtle, Screen

# turtle object, saved into a variable called timmy
timmy = Turtle()
timmy.shape("turtle")  # change shape
timmy.color("coral")  # change color
timmy.forward(100)

print(timmy)  # <turtle.Turtle object at 0x0000026F94BDFE10>

# object.<attribute>

my_screen = Screen()
print(my_screen.canvwidth)
print(my_screen.canvheight)

# object.<method()>
my_screen.exitonclick()
