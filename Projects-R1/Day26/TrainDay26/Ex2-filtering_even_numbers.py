# Instructions
# You are going to write a List Comprehension to create a new list called result. This new list should only contain
# the even numbers from the list numbers.
#
# DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.
#
# Example Output
# [2, 8, 34]
# Hint
# Use the keyword method for starting the List comprehension and fill in the relevant parts.
# Even numbers can be divided by 2 with no remainder.
# Remind yourself of how the modulo operator works.


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:

result = [number for number in numbers if number % 2 == 0]

# Write your code 👆 above:

print(result)
