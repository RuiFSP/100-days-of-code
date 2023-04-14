import turtle


class Layout(turtle.Turtle):
    """
    This class sets up the game window and background.
    """

    def __init__(self) -> None:
        super().__init__()
        self.screen = turtle.Screen()
        self.width = 600
        self.height = 600
        self.screen.setup(width=self.width, height=self.height)
        self.screen.bgcolor("black")
        self.screen.bgpic("images/background.gif")
        self.screen.title("Space Invaders")

        self.border_pen = turtle.Turtle()
        self.border_pen.speed(0)
        self.border_pen.color("white")
        self.border_pen.penup()
        self.border_pen.setposition(-300, -300)
        self.border_pen.pendown()
        self.border_pen.pensize(3)
        for _ in range(4):
            self.border_pen.fd(600)
            self.border_pen.lt(90)
        self.border_pen.hideturtle()
