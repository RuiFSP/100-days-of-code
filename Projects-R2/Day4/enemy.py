import turtle
import random


class Enemy:
    """
    A class representing an enemy in the game.

    Attributes
    ----------
    space_enemy : turtle.Turtle
        The turtle object representing the enemy.
    enemy_speed : int
        The speed at which the enemy moves horizontally.

    Methods
    -------
    move_enemy() -> None:
        Moves the enemy horizontally across the screen and changes direction when it reaches the screen's edge.
    """
    def __init__(self) -> None:
        """
        Initializes the Enemy class by creating the turtle object, setting its initial position,
        and defining its speed.
        """
        turtle.register_shape("images/invader.gif")
        self.space_enemy: turtle.Turtle = turtle.Turtle()
        self.space_enemy.color("red")
        self.space_enemy.shape("images/invader.gif")
        self.space_enemy.penup()
        self.space_enemy.speed(0)
        x: int = random.randint(-200, 200)
        y: int = random.randint(100, 250)
        self.space_enemy.setposition(x, y)
        self.enemy_speed: int = 2

    def move_enemy(self) -> None:
        """
        Moves the enemy horizontally across the screen and changes direction when it reaches the screen's edge.
        """
        x: float = self.space_enemy.xcor()
        x += self.enemy_speed
        self.space_enemy.setx(x)

        if self.space_enemy.xcor() > 280:
            self.space_enemy.sety(self.space_enemy.ycor() - 40)
            self.enemy_speed *= -1

        if self.space_enemy.xcor() < -280:
            self.space_enemy.sety(self.space_enemy.ycor() - 40)
            self.enemy_speed *= -1
