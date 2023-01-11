import random
from art import logo
from os import system

play_game = True
should_play = True
player_inplay = True
dealer_inplay = True
dealer_hand = []
player_hand = []


def get_random_card():
    '''
    :return: random card from cards
    '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def get_score(array):
    '''
    Takes the array of cards and returns the sum
    :param array:
    :return: sum of elements
    '''
    return sum(array)


def print_current_result():
    '''
    Prints the initial conditions
    :return: player hand and dealer's first card
    '''
    print(f"\tYour cards: {player_hand}, current score: {get_score(player_hand)}")
    print(f"\tComputer's first card: {dealer_hand[0]}")


def print_final_result():
    '''
    :return: the prints of final hand for player and computer
    '''
    print(f"\tYour final hand: {player_hand}, final score: {get_score(player_hand)}")
    print(f"\tComputer's final hand: {dealer_hand}, final score: {get_score(dealer_hand)}")


def check_blackjack():
    '''
    check if player winning hand is a blackjack, if not just returns the win
    :return: the print for blackjack or simply win
    '''
    if get_score(player_hand) > get_score(dealer_hand) and len(player_hand) == 2 and get_score(player_hand) == 21:
        print("Win with Blackjack 😎")
    else:
        print("You win 😀")


def reset_game():
    '''
    resets global variables to start a new game
    :return: all
    '''
    global dealer_hand
    global player_hand
    global should_play
    global dealer_inplay
    global player_inplay

    player_hand = []
    dealer_hand = []
    player_inplay = True
    dealer_inplay = True
    should_play = True


while play_game:
    print(logo)

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':

        reset_game()

        while should_play:

            if dealer_hand == [] and player_hand == []:
                # initial hand
                for _ in range(2):
                    dealer_hand.append(get_random_card())
                    player_hand.append(get_random_card())

                print_current_result()

            if input("Type 'y' to get another card, type 'n' to pass:") == 'y':
                player_hand.append(get_random_card())
                print_current_result()
                if get_score(player_hand) > 21:
                    player_inplay = False
                    print("You lose 😥")
                    should_play = False
            else:

                if get_score(dealer_hand) < 17:
                    while get_score(dealer_hand) < 17:
                        dealer_hand.append(get_random_card())
                        if get_score(dealer_hand) > 21:
                            dealer_inplay = False
                if not dealer_inplay:
                    print_final_result()
                    check_blackjack()
                elif get_score(dealer_hand) < get_score(player_hand) <= 21:
                    print_final_result()
                    check_blackjack()
                elif get_score(dealer_hand) == get_score(player_hand) and get_score(player_hand) <= 21:
                    print_final_result()
                    print("You Draw 😑")
                else:
                    print_final_result()
                    print("You lose 😥")

                should_play = False

    else:
        play_game = False
        system("cls()")
        print("Goodbye, see you next time 😀")
