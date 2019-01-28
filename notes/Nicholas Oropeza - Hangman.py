import string
import random

word_bank = ["katakana", "Japan", "Moscow", "block",
             "No one expects the Spanish Inquisition.",
             "mouse", "turquoise", "concatenation", "jukebox",
             "Nintendo Switch", "artificial", "intelligence",
             "How are you today?", "This is a sea urchin."]

word = random.choice(word_bank)
guessed = []
blank = []
guesses = 8
playing = True

print("Welcome to Hangman")
print()
print(word)
for i in range(len(word)):
        if word[i] in list(string.ascii_letters):
            blank.append('_')
        elif word[i] == ' ':
            blank.append(' ')
        elif word[i] == '.':
            blank.append('.')
        elif word[i] == '.':
            blank.append('.')

while guesses > 0 and playing:
    letter = input("Enter the letter or word")
    guessed.append(letter)
    print(guessed)
    print("".join(blank))

    for i in range(len(blank)):
        if letter in list(blank):
            blank.insert(i, letter)
            print("".join(blank))

    if letter.lower() in word:
        blank.insert(i, letter)
        print("".join(blank))
        print("Correct")
        print("You have %d guesses left." % guesses)
    else:
        guesses -= 1
        print("Wrong")
        print("You have %d guesses left." % guesses)

    if guessed == word:
        print("You guessed right, good job.")
        playing = False

    if letter == word:
        print("You guessed right, good job.")
        playing = False

    if guesses == 0:
        print("The word/phrase was '%s'" % word)
#     elif letter in list(string.ascii_uppercase) and word:
#         blank.insert(i, letter)
#         print("".join(blank))
#         print("Correct")
#         print("You have %d guesses left." % guesses)
