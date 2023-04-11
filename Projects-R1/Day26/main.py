# task1 1. Create a dictionary from .csv in this format: {"A": "Alfa", "B": "Bravo"}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# task 2. create a list of the phonetic code words from a word the user input:

user_input = input("Enter a word: ").upper()

output_list = [new_dict.get(letter) for letter in user_input if letter.isalpha()]

print(output_list)
