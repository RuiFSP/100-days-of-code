# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo

# Global variables
PC_NUMBER = randint(1, 100)
play_game = False
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
num_attempts = 0

print(logo)
print("Welcome to the Number Guess Game!")
print("I'm thinking of a number between 1 and 100")

# print(PC_NUMBER)

player_difficulty = input("Choose a difficulty. type 'easy' or 'hard': ").lower()


def update_attempts():
    return num_attempts - 1


def end_game():
    global play_game
    play_game = False
    return False


def check_answer():
    if player_guess > PC_NUMBER:
        print("Too high\nGuess again.")
    elif player_guess < PC_NUMBER:
        print("Too low\nGuess again.")
    else:
        print(f"You got it! The answer was {PC_NUMBER}")


while not play_game:
    if player_difficulty == "easy":
        num_attempts = EASY_ATTEMPTS
        play_game = True
    elif player_difficulty == 'hard':
        num_attempts = HARD_ATTEMPTS
        play_game = True
    else:
        print("invalid choice")
        break

while play_game:
    print(f"You have {num_attempts} remaining to guess the number")
    player_guess = int(input("Make a guess: "))
    check_answer()

    if player_guess == PC_NUMBER:
        end_game()

    num_attempts = update_attempts()

    if num_attempts == 0:
        print("You've run out of guesses, you lose.")
        play_game = end_game()
