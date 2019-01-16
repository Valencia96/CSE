import string
import random
"""
print(list(string.ascii_letters))
print(string.digits)
print(string.punctuation)
"""
word_bank = ["katakana", "Japan", "Moscow", "block",
             "No one expects the Spanish Inquisition.",
             "mouse", "turquoise", "concatenation", "jukebox",
             "Nintendo Switch", "artificial", "intelligence",
             "How are you today?", "This is a sea urchin.",
             "Super Mario Bros. 2, GOTY Since 1988."]

pesto = random.choice(word_bank)
letters_guessed = []
hidden_word = len(pesto)
guesses = 8
playing = True

while guesses > 0 and playing:
    letter = input("Enter the letter or word")
    letters_guessed.append(letter)
    print(letters_guessed)

    for i in range(len(pesto)):  # i goes through all indices
        if pesto[0] == string.ascii_letters:  # if we find a letter
            pesto.pop(i)  # remove the i-th index
            pesto.insert(i, "_")  # Put a _ there instead
            print(pesto)
    guesses -= 1
