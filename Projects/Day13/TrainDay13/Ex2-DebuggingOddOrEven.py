# Instructions
# Read this the code in main
# Spot the problems 🐞.
# Modify the code to fix the program.
# Fix the code so that it works and passes the tests when you submit.
#
# Hint
# Review the previous lesson and go through the 10 steps to tackle these debugging problems.

# Initial code
# number = int(input("Which number do you want to check?"))
#
# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")


# Problem: incorrect verification number % 2 = 0 - IDE highlights

# corrected code

number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
