import turtle
import math
import random

from layout import Layout
from scoreboard import Scoreboard
from player import Player
from bullet import Bullet
from enemy import Enemy

ENEMY_MIN_X: int = -200
ENEMY_MAX_X: int = 200
ENEMY_MIN_Y: int = 100
ENEMY_MAX_Y: int = 250
BULLET_DISTANCE: int = 20
SCORE_INCREMENT: int = 10
SCREEN_HEIGHT: int = 600


def is_collision(turtle1: turtle.Turtle, turtle2: turtle.Turtle) -> bool:
    """Check if two turtles collide.

    Args:
        turtle1: The first turtle.
        turtle2: The second turtle.

    Returns:
        True if the turtles collide, False otherwise.
    """
    distance = math.sqrt(
        math.pow(turtle1.xcor() - turtle2.xcor(), 2) +
        math.pow(turtle1.ycor() - turtle2.ycor(), 2)
    )
    return distance < BULLET_DISTANCE


class Game:
    """The main game class.

    Attributes:
        screen: The game screen layout.
        bullet: The player's bullet.
        player: The game's player.
        enemy: The game's enemy.
        scoreboard: The game's scoreboard.
    """

    def __init__(self):
        """Initialize the game."""
        self.screen = Layout()
        self.bullet = Bullet()
        self.player = Player(self.bullet)
        self.enemy = Enemy()
        self.scoreboard = Scoreboard()

        turtle.listen()
        turtle.onkey(self.player.move_left, "Left")
        turtle.onkey(self.player.move_right, "Right")
        turtle.onkey(self.bullet.move_bullet, "space")

        self.run_game()

    def run_game(self):
        """Run the game loop."""
        while True:
            self.enemy.move_enemy()
            self.bullet.move_bullet()

            if is_collision(self.bullet.space_bullet, self.enemy.space_enemy):
                self.handle_bullet_collision()

            if is_collision(self.player.space_enemy, self.enemy.space_enemy):
                self.handle_game_over()
                break

    def move_player_left(self):
        """Move the player left."""
        x = self.player.space_enemy.xcor()
        x -= self.player.player_speed
        if x < -280:
            x = -280
        self.player.space_enemy.setx(x)

    def move_player_right(self):
        """Move the player right."""
        x = self.player.space_enemy.xcor()
        x += self.player.player_speed
        if x > 280:
            x = 280
        self.player.space_enemy.setx(x)

    def handle_bullet_collision(self):
        """Handle bullet collision with the enemy."""
        self.bullet.space_bullet.hideturtle()
        self.bullet.bullet_state = "ready"
        self.bullet.space_bullet.setposition(0, -SCREEN_HEIGHT / 2)
        self.enemy.space_enemy.setposition(
            random.randint(ENEMY_MIN_X, ENEMY_MAX_X),
            random.randint(ENEMY_MIN_Y, ENEMY_MAX_Y)
        )
        self.scoreboard.update_score(SCORE_INCREMENT)

    def handle_game_over(self):
        """Handle game over."""
        self.player.space_enemy.hideturtle()
        self.enemy.space_enemy.hideturtle()
        print("Game Over")


if __name__ == "__main__":
    game = Game()
