from art import logo
from os import system

print(logo)
print("Welcome to the secret auction program")

auction = True
bids = {}


def find_highest_bid():
    max_bid = 0
    winning_bid_person = ""

    for people in bids:
        if bids[people] > max_bid:
            max_bid = bids[people]
            winning_bid_person = people

    print(f"The winner is {winning_bid_person} with a bid of ${max_bid}.\n")


while auction:

    name = input("What is your name: ")
    bid = int(input("What's your bid?: $"))

    bids[name] = bid

    response = input("Are there any other bidders Type 'yes or 'no'.\n").lower()

    # Modify run configurations -> execution -> emulate terminal in output console
    if response == 'yes':
        system("cls()")
    elif response == 'no':
        auction = False
        find_highest_bid()
