import time
import tkinter as tk

import winsound

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
                   '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                   ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
                   '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' '}

# Constants
BEEP_FREQUENCY = 1000
DOT_BEEP_DURATION = 250
DASH_BEEP_DURATION = 750
WORD_PAUSE_DURATION = 0.4


def convert_to_morse_code(text: str) -> str:
    """
    Convert a text string to Morse code.

    Args:
        text (str): The text to convert to Morse code.

    Returns:
        str: The Morse code string.
    """
    morse_code = [MORSE_CODE_DICT.get(char.upper(), '?') for char in text]
    print(f"This is your text converted into morse code: {' '.join(morse_code)}")
    return ' '.join(morse_code)


def play_morse_code(morse_code: str, text: str):
    """
    Play the Morse code string as beeps.

    Args:
        morse_code (str): The Morse code string.
        text (str): The original text string.
    """
    print("Playing your Morse code: ", end=' ')
    try:
        for symbol in morse_code:
            print(symbol, end=' ')
            if symbol == ".":
                if text and text[0].isalnum() and text[0].upper() in MORSE_CODE_DICT:
                    text = text[1:]
                winsound.Beep(BEEP_FREQUENCY, DOT_BEEP_DURATION)
            elif symbol == "-":
                if text and text[0].isalnum() and text[0].upper() in MORSE_CODE_DICT:
                    text = text[1:]
                winsound.Beep(BEEP_FREQUENCY, DASH_BEEP_DURATION)
            elif symbol == " ":
                time.sleep(WORD_PAUSE_DURATION / 1000)
            else:
                raise ValueError(f"Invalid Morse code symbol: {symbol}")
    except Exception as e:
        print(f"Error during playback: {e}")
    else:
        print("Finished playing Morse code.")


def convert_and_play():
    """
    Converts text to Morse code and plays it using the play_morse_code function.

    Raises:
        ValueError: If text entry field is empty or failed to convert text to Morse code.

    Returns:
        None
    """
    try:
        # Get input text from the entry field
        input_text = text_entry_field.get()

        # Check if the input text is empty
        if not input_text:
            raise ValueError("Text entry is empty")

        # Remove spaces from the input text
        text_without_spaces = input_text.replace(" ", "")

        # Convert the text to morse code
        morse_code = convert_to_morse_code(text_without_spaces)

        # Check if the conversion was successful
        if not morse_code:
            raise ValueError("Failed to convert text to Morse code")

        # Play the morse code and show a success message
        play_morse_code(morse_code, text_without_spaces)
        success_message_label.config(text="Conversion successful!")
        success_message_label.pack()

    except ValueError as e:
        # Show an error message if there was a problem
        error_message_label.config(text=str(e))


window = tk.Tk()
window.title("Morse Code Converter")

# Create a label for the input text
text_frame = tk.Frame(window)
text_frame.pack(padx=10, pady=10)

text_label = tk.Label(text_frame, text="Enter text to convert to Morse code:")
text_label.pack(side=tk.LEFT)

text_entry_field = tk.Entry(text_frame, width=50)
text_entry_field.pack(side=tk.LEFT, padx=10)

# Create a frame for the button and error message label
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

play_button = tk.Button(button_frame, text="Convert and Play", command=convert_and_play)
play_button.pack(side=tk.LEFT, padx=10)

error_message_label = tk.Label(button_frame, text="", fg="red")
error_message_label.pack(side=tk.LEFT)

success_message_label = tk.Label(window, text="", fg="green")

window.mainloop()
