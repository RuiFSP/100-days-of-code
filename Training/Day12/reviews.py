################### Scope ####################

# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# ------------------------------------------------

# # Local Scope
# # exists inside functions
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength) # not defined outside of function

# ------------------------------------------------

# Global Scope
# player_health = 10
#
#
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#
#     drink_potion()
#
#
# print(player_health)

# ------------------------------------------------

# There is no Block Scope (for , if, while, ...)
# Block scope such as (for, if , while) does not exist in python, different in language such as java, javascript


# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]
#
# print(new_enemy) -> this codeis still valid


# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#
# print(new_enemy)  # this code now does not have access to new enemy - NameError

# ------------------------------------------------

# Modify global scope
# enemies = 1
# print(f"initial enemies outside function: {enemies}")
#
#
# def increase_enemies():
#     global enemies  # we need to explicit say there is a global variable - this is considered a bad practice
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
#
# def increase_enemies_solution():
#     return enemies + 1
#
#
# enemies = increase_enemies_solution()
# print(f"enemies outside function with correct approach: {enemies}")

# Global constants
# values that won't be changed
# naming convention to global constants is uppercase
# PI = 4.14159
# URL: "http://www.google.com"
# TWITTER_HANDLE = "@RuiFSPinto"
#
#
# def calc():
#     return TWITTER_HANDLE
