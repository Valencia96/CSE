import random
playing = True
guesses_left = 6
guessed_letters = []
# guess = input("Guess a letter")
words = ["Germany", "North Korea", "South Korea",
         "Japan", "Mexico", "Australia", "Canada"]

for character in words:
    if character == "u":
        current_index = words.index(characters)
        words.pop(current_index)
        words.insert(current_index, "*")
