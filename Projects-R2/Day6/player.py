import turtle
from bullet import Bullet


class Player:
    """
    Represents the player in the game
    """

    def __init__(self, bullet: Bullet):
        """
        Initializes the player's attributes

        Args:
            bullet (Bullet): A bullet object that can be fired by the player
        """
        turtle.register_shape("assets/player.gif")
        self.space_enemy: turtle.Turtle = turtle.Turtle()
        self.space_enemy.color("blue")
        self.space_enemy.shape("assets/player.gif")
        self.space_enemy.penup()
        self.space_enemy.speed(0)
        self.space_enemy.setposition(0, -250)
        self.space_enemy.setheading(90)

        self.player_speed: int = 15
        self.bullet: Bullet = bullet

        turtle.listen()
        turtle.onkey(self.move_left, "Left")
        turtle.onkey(self.move_right, "Right")
        turtle.onkey(self.fire_bullet, "space")

    def move_left(self) -> None:
        """
        Move the player's turtle to the left and prevent it from going off the screen
        """
        x: float = self.space_enemy.xcor()
        x -= self.player_speed
        if x < -280:
            x = -280
        self.space_enemy.setx(x)
        print("Player position:", self.space_enemy.position())

    def move_right(self) -> None:
        """
        Move the player's turtle to the right and prevent it from going off the screen
        """
        x: float = self.space_enemy.xcor()
        x += self.player_speed
        if x > 280:
            x = 280
        self.space_enemy.setx(x)
        print("Player position:", self.space_enemy.position())

    def fire_bullet(self) -> None:
        """
        Fire a bullet from the player's position
        """
        print("Firing bullet")
        if self.bullet.bullet_state == "ready":
            self.bullet.bullet_state = "fire"
            x: float = self.space_enemy.xcor()
            y: float = self.space_enemy.ycor() + 10
            print("Bullet position:", (x, y))
            self.bullet.space_bullet.setposition(x, y)
            self.bullet.space_bullet.showturtle()
            print("Bullet position:", self.bullet.space_bullet.position())
