

# transform names into a list
# ['Aang\n', 'Zuko\n', 'Appa\n', 'Katara\n', 'Sokka\n', 'Momo\n', 'Uncle Iroh\n', 'Toph']
with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()

# loop each letter and substitute each [name]
with open("./Input/Letters/starting_letter.txt") as letter_file:
    dedicated_letter = letter_file.read()
    for name in names_list:
        stripped_name = name.strip()
        personalized_letter = dedicated_letter.replace("[name]", stripped_name)

        # write and save the modified latter
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as finished_letter:
            finished_letter.write(personalized_letter)
