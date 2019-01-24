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

word = random.choice(word_bank)
letters_guessed = []
blank = []
guesses = 8
playing = True

print("Welcome to Hangman")

while guesses > 0 and playing:
    letter = input("Enter the letter or word")

    if letter in blank:
        blank.append(letter)
    else:
        print(letters_guessed)

    letters_guessed.append(letter)

    for i in range(len(word)):
        if word[i] in list(string.ascii_letters):
            blank.append(word)
        elif word[i] == " ":
            blank.append(" ")
        else:
            blank.append("*")

    if letter == word:
        print("You guessed right, good job.")
        playing = False

    if letter in word:
        print("Correct")
        print("You have %d guesses left." % guesses)
    elif letter in list(string.ascii_uppercase) and word:
        print("Correct")
        print("You have %d guesses left." % guesses)
    else:
        guesses -= 1
        print("Wrong")
        print("You have %d guesses left." % guesses)

    if guesses == 0:
        print("The word/phrase was '%s'" % word)
