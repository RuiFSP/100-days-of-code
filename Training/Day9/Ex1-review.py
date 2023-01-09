programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something"}

# retrieve by key
# print(programming_dictionary["Bug"])

# Adding new items to dictionary

# print(programming_dictionary)

# create an empty dictionairy
empty_dictionary = {}

# Wipe and existing dictionairy
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionay
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# Loop through a dictionary
# just keys
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# Nesting Lists and Dictionaries
# {
#     key: [List]
#     key1: {Dict}
# }

###########################################
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting Dictionary in a Dictionary
travel_log1 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 15
    },
}

print(travel_log1)

# Nesting Dictionaries in a list
# [{
#     key: [List],
#     key1: {Dict},
# },
# [{
#     key: value,
#     key1: value,
# }]

travel_log2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 15
    },
]
