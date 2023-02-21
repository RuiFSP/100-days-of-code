############DEBUGGING#####################

# # Describe Problem
# # Problem was in range. When i = 20, needs to print, but range was [1,20[ and the upper bound normally is omitted
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
# my_function()

# # Reproduce the Bug
# # Problem was IndexError, basically sometimes the randint = 6, but list only have up to index 5
# from random import randint
#
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# # There was a problem in upper limit for millennial < 1994, it will fail for year = 1994
# year = int(input("What's your year of birth?"))
# if 1980 < year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# # Fix the Errors
# # Problem1: print was highlighted, because it expected an indentation
# # Problem2: input is a string and if compares int, need to convert str into int
# # Problem3: print statement is referencing a variable without fstring
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# # Print is Your Friend
# # Problem1 :word_per_page, was not saving the input value, if was comparing ==. Prints helped discover
# # Problem2 :no need to initialize variables , since we can directly save the inputs pages and words_per_page = 0
# # pages = 0
# # word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# print(total_words)

# Use a Debugger
# Problem1: we provide a list and want to multiply each element by 2, and save them in a new list. It is only storing
# the last value 13*3, because of incorrect indentation. I we want to save all values, appended must be in the
# for block scope
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])
