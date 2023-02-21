# Instructions
# You are going to write a program that will mark a spot with an X.
#
# In the starting code, you will find a variable called map.
#
# This map contains a nested list. When map is printed this is what the nested list looks like:
#
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
#
# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}"
# to format the 3 lists to be printed as a 3 by 3 square, each on a new line.
#
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
#
# Now it looks a bit more like the coordinates of a real map:
#
#
#
# Your job is to write a program that allows you to mark a square on the map using a two-digit system.
#
# The first digit in the input will specify the column (the position on the horizontal axis).
#
# The second digit in the input will specify the row number (the position on the vertical axis).
#
# So an input of 23 should place an X at the position shown below:
#
#
#
# First, your program must take the user input and convert it to a usable format.
#
# Next, you need to use that input to update your nested list with an "x". Remember that your nested list map actually
# looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].
#
# Example Input 1
# column 2, row 3 would be entered as:
#
# 23
# Example Output 1
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']
# Example Input 2
# column 3, row 1 would be entered as:
#
# 31
# Example Output 2
# ['⬜️', '⬜️', 'X']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']


# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
col_coord = int(position[1])
row_coord = int(position[0])

map[col_coord-1][row_coord-1] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
