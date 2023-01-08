# STEP2

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
user_text = input("Type your message:\n").lower()
shift_amount = int(input("Type the shift number:\n"))


def encrypt(user_text, shift_amount):
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


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(user_text, shift_amount):
    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
    #  amount and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"
    my_list_decrypted_letters = []
    for i in range(0, len(user_text)):
        if user_text[i] in alphabet:
            new_index = alphabet.index(user_text[i]) - shift_amount
            if new_index < 0:
                new_index = alphabet.index(user_text[i]) - shift_amount + len(alphabet)

            my_list_decrypted_letters.append(alphabet[new_index])
        else:
            my_list_decrypted_letters.append(user_text[i])

    cipher_text = ''.join(my_list_decrypted_letters)
    print(f"The decoded text is {cipher_text}")


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call
#  the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND*
#  decrypt a message.


if direction == "encode":
    encrypt(user_text, shift_amount)
elif direction == "decode":
    decrypt(user_text, shift_amount)
else:
    print("wrong option")
