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

test = "Uganda"
pesto = list(test)
"""
for character in word:
    if character == "u":
        current_index = word.index(character)
        word.pop(current_index)
        word.insert(current_index, "*")
"""

for i in range(len(pesto)):  # i goes through all indices
    if pesto[1] == "u":  # if we find a U
        test_bank.pop(i)  # remove the i-th index
        test_bank.insert(i, "_")  # Put a * there instead
print(pesto)
