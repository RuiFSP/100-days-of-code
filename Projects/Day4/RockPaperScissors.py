rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

# rules
# rock > scissors
# paper > rock
# scissors > paper

# player_choice
player_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_pick == 0:
    print(rock)
elif player_pick == 1:
    print(paper)
elif player_pick == 2:
    print(scissors)
else:
    print("Wrong option")

# computer_choice
random_generated_pick_from_computer = random.randint(0, 2)

if random_generated_pick_from_computer == 0:
    print("Computer chose:\n" + rock)
elif random_generated_pick_from_computer == 1:
    print("Computer chose:\n" + paper)
elif random_generated_pick_from_computer == 2:
    print("Computer chose:\n" + scissors)
else:
    print("Wrong option")

# result
if player_pick == random_generated_pick_from_computer:
    print("It is a draw")
elif player_pick == 0 and random_generated_pick_from_computer == 2 or player_pick == 1 and random_generated_pick_from_computer == 0 or player_pick == 2 and random_generated_pick_from_computer == 1:
    print("You win")
elif player_pick == 0 and random_generated_pick_from_computer == 1 or player_pick == 1 and random_generated_pick_from_computer == 2 or player_pick == 2 and random_generated_pick_from_computer == 0:
    print("You lose")
else:
    print("Provided the correct options")
