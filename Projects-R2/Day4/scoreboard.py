import turtle


class Scoreboard:
    '''
    The Scoreboard class initializes the score and writes it on the screen.

    Attributes:
    -----------
    score : int
        The current score.
    score_pen : turtle.Turtle
        The turtle used for writing the score.
    score_string : str
        The string used to display the score on the screen.

    Methods:
    --------
    update_score(new_score: int) -> None
        Updates the score with the given value and updates the display on the screen.
    '''

    def __init__(self) -> None:
        """
        Initializes a new Scoreboard object.
        """
        self.score: int = 0
        self.score_pen: turtle.Turtle = turtle.Turtle()
        self.score_pen.speed(0)
        self.score_pen.color("white")
        self.score_pen.penup()
        self.score_pen.setposition(-290, 260)
        self.score_string: str = "Score: %s" % self.score
        self.score_pen.write(self.score_string, False, align="left", font=("Arial", 14, "normal"))
        self.score_pen.hideturtle()

    def update_score(self, new_score: int) -> None:
        """
        Updates the score with the given value and updates the display on the screen.

        Parameters:
        -----------
        new_score : int
            The amount by which to increase the score.
        """
        self.score += new_score
        self.score_string = "Score: %s" % self.score
        self.score_pen.clear()
        self.score_pen.write(self.score_string, False, align="left", font=("Arial", 14, "normal"))
