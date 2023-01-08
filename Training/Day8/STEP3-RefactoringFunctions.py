# STEP 3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caeser(user_text, shift_amount, direction_choice):
    my_text = []

    if direction_choice == "decode":
        shift_amount *= -1

    for letter in user_text:
        if letter in alphabet:
            letter_position = alphabet.index(letter)

            new_letter_position = letter_position + shift_amount

            if new_letter_position > 26:
                new_letter_position = alphabet.index(letter) + shift_amount - len(alphabet)
                my_text.append(alphabet[new_letter_position])

            elif new_letter_position < 0:
                new_letter_position = letter_position + shift_amount
                my_text.append(alphabet[new_letter_position])
            else:
                my_text.append(alphabet[new_letter_position])
        else:
            my_text.append(letter)

    cipher_text = ''.join(my_text)
    print(f"Here's the {direction_choice}d result: {cipher_text}")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caeser(user_text=text, shift_amount=shift, direction_choice=direction)
