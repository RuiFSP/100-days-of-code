# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
from letters import alphabet

# Logo game
print(logo)


def caeser(user_text, shift_amount, direction_choice):
    my_text = []

    if direction_choice == "decode":
        shift_amount *= -1

    for char in user_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if char in alphabet:
            letter_position = alphabet.index(char)

            new_letter_position = letter_position + shift_amount

            if new_letter_position > 26:
                new_letter_position = alphabet.index(char) + shift_amount - len(alphabet)
                my_text.append(alphabet[new_letter_position])

            elif new_letter_position < 0:
                new_letter_position = letter_position + shift_amount
                my_text.append(alphabet[new_letter_position])
            else:
                my_text.append(alphabet[new_letter_position])
        else:
            my_text.append(char)

    cipher_text = ''.join(my_text)
    print(f"Here's the {direction_choice}d result: {cipher_text}")


# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
response = True

while response:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    shift %= 25

    caeser(user_text=text, shift_amount=shift, direction_choice=direction)

    result = input("Type 'yes if you want to go again. Otherwise type 'no'\n")

    if result == "no":
        response = False
        print("Goodbye")
