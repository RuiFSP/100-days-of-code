import turtle


class Bullet:
    def __init__(self):
        """Initialize Bullet class."""
        self.space_bullet: turtle.Turtle = turtle.Turtle()
        self.space_bullet.color("yellow")
        self.space_bullet.shape("square")
        self.space_bullet.penup()
        self.space_bullet.speed(0)
        self.space_bullet.setheading(90)
        self.space_bullet.shapesize(0.5, 0.5)
        self.space_bullet.hideturtle()

        self.bullet_speed: int = 20
        self.bullet_state: str = "ready"

    def move_bullet(self) -> None:
        """Move bullet."""
        if self.bullet_state == "fire":
            x: float = self.space_bullet.xcor()
            y: float = self.space_bullet.ycor() + self.bullet_speed
            self.space_bullet.setposition(x, y)

        if self.space_bullet.ycor() > 275:
            self.space_bullet.hideturtle()
            self.bullet_state = "ready"
            self.space_bullet.setposition(0, -400)
