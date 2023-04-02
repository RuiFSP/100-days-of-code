from typingtest import TypingTestApp
import random

# Sample text
text = "The quick brown fox jumps over the lazy dog. " \
       "A rolling stone gathers no moss. " \
       "All is fair in love and war. " \
       "Actions speak louder than words. " \
       "You can't judge a book by its cover."

# Create a list of phrases by splitting the sample text on '.'
phrases = text.split('.')

# Generate a random phrase
random_phrase = random.choice(phrases)


if __name__ == "__main__":
    typing_test = TypingTestApp(random_phrase)
    typing_test.run()

