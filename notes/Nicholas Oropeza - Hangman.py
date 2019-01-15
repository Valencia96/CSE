import string
import random
"""
print(list(string.ascii_letters))
print(string.digits)
print(string.punctuation)
"""
letters_guessed = []
guesses = 8
playing = True
word_bank = ["katakana", "Japan", "Moscow", "block",
             "No one expects the Spanish Inquisition.",
             "mouse", "turquoise", "concatenation", "jukebox",
             "Nintendo Switch", "artificial", "intelligence",
             "How are you today?", "This is a sea urchin.",
             "Super Mario Bros. 2, GOTY Since 1988."]

# test = "Uganda"
pesto = random.choice(word_bank)

if guesses > 0:
    """
    letter = input("Enter the letter or word")
    letters_guessed.append(letter)
    print(letters_guessed)
    """
    for character in pesto:
        if character == string.ascii_letters:
            current_index = pesto.index(character)
            pesto.pop(current_index)
            pesto.insert(current_index, "_")
    guesses -= 1
print(pesto)
