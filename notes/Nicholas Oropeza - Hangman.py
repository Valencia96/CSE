import random

letters_guessed = []
guesses = 8
playing = True
word_bank = ["katakana", "Japan", "Moscow", "block",
             "No one expects the Spanish Inquisition.",
             "mouse", "turquoise", "concatenation", "jukebox",
             "Nintendo Switch", "artificial", "intelligence",
             "How are you today?", "This is a sea urchin.",
             "Super Mario Bros. 2, GOTY Since 1988."]

word = random.choice(word_bank)
print(word)
