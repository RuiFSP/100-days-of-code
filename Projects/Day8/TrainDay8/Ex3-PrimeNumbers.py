# Instructions
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
#
# https://en.wikipedia.org/wiki/Prime_number
#
# You need to write a function that checks whether if the number passed into it is a prime number or not.
#
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
#
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# check up to 100


# Write your code below this line 👇
my_prime_list = [2, 3]

for number in range(3, 101):
    if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        my_prime_list.append(number)


def prime_checker(number):
    if number in my_prime_list:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# alternative solutions
def prime_checker_1(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
prime_checker_1(number=n)
