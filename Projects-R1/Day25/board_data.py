from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 8, 'normal')


class BoardData(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.list_correct_guesses = []

    def add_correct_guess(self, user_guess):
        self.list_correct_guesses.append(user_guess)

    def add_name_to_map(self, x_coord, y_coord, user_guess):
        self.goto(x_coord, y_coord)
        self.write(f"{user_guess}", align=ALIGNMENT, font=FONT)
