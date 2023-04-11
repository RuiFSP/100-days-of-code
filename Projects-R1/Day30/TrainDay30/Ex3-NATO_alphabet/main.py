# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# while version

# valid_input -> True
# while valid_input:
#
#     word = input("Enter a word: ").upper()
#
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         continue
#
#     else:
#         print(output_list)
#         valid_input = False

# recursive version

def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()

    else:
        print(output_list)


generate_phonetic()
