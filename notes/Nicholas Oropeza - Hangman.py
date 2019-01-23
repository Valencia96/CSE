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
             "How are you today?", "This is a sea urchin."]

random_choice = random.choice(word_bank)
letters_guessed = []
blank = []
guesses = 8
playing = True

print("Welcome to Hangman")

for i in range(len(random_choice)):
    if random_choice[i] in list(string.ascii_letters):
        blank.append(random_choice)
    elif random_choice[i] == "":
        blank.append(" ")
    else:
        blank.append("_")

while guesses > 0 and playing:
    letter = input("Enter the letter or word")
    letters_guessed.append(letter)
    print(letters_guessed)
    print()

    for i in range(len(random_choice)):
        if random_choice[i] in list(string.punctuation):
            blank.append(random_choice)
        else:
            blank.append("_")

    if letter == random_choice:
        print("You guessed right, good job.")
        playing = False

    if letter in random_choice:
        print("Correct")
    else:
        guesses -= 1

    if guesses == 0:
        print("The word/phrase was '%s'" % random_choice)
