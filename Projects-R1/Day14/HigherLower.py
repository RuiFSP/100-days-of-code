import random
import art
from os import system
from game_data import data

# Lower higher is a game where you have to guess which social media celebrity has more followers


# Global Variables
game_score = 0
my_dict = random.sample(data, 2)


# Functions
def random_data_pick():
    """
    :return: 1 random celebrity dictionary, from data list [{},{}...{}]
    """
    return random.choice(data)


def pop_add_data():
    """
    removes first element of list and populates again with a random celebrity pick
    """
    my_dict.pop(0)
    my_dict.append(random_data_pick())


def verify_duplicate_pick():
    """
    verifies if the list is not duplicated
    :return: list without duplicates
    """
    while my_dict[0]['name'] == my_dict[1]['name']:
        pop_add_data()

    return my_dict


def compare_followers(user_pick, celeb_a, celeb_b):
    if user_pick == 'A' and celeb_a['follower_count'] > celeb_b['follower_count']:
        return 1
    elif user_pick == 'B' and celeb_a['follower_count'] < celeb_b['follower_count']:
        return 1
    else:
        return -1


def format_data(account):
    """
    :param account: celebrity data to format
    :return: f string with name, description and country
    """
    return f"{account['name']}, a {account['description']}, from {account['country']}."


while game_score >= 0:

    system("cls()")
    print(art.logo)
    verify_duplicate_pick()
    print(f"Compare A: {format_data(account=my_dict[0])}")
    print(art.vs)
    print(f"Against B: {format_data(account=my_dict[1])}")
    choice = input(f"Who has more followers? type 'A or 'B: ").upper()

    result = compare_followers(user_pick=choice, celeb_a=my_dict[0], celeb_b=my_dict[1])

    if result == 1:
        game_score += result
        print(f"You're are right! Current score: {game_score}\n")
        pop_add_data()

    else:
        print(f"Sorry, that's wrong. Final score: {game_score}\n")
        if input("Duo you want to play again ? Type 'y' or 'n'").lower() == "y":
            game_score = 0
            pop_add_data()
        else:
            game_score = result
