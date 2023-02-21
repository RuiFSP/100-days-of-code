# STEP1

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
user_text = input("Type your message:\n").lower()
shift_amount = int(input("Type the shift number:\n"))


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(user_text, shift_amount):
    # Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the
    # shift amount and print the encrypted text.
    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


    my_list_encrypted_letters = []

    for i in range(0, len(user_text)):
        if user_text[i] in alphabet:
            new_index = alphabet.index(user_text[i]) + shift_amount
            if new_index > 26:
                new_index = alphabet.index(user_text[i]) + shift_amount - len(alphabet)
            my_list_encrypted_letters.append(alphabet[new_index])
        else:
            my_list_encrypted_letters.append(user_text[i])

    cipher_text = ''.join(my_list_encrypted_letters)
    print(f"The encoded text is {cipher_text}")


# Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt
# a message.
encrypt(user_text, shift_amount)
