import string
import random

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
print()

while guesses > 0 and playing:
    letter = input("Enter the letter or word")
    letters_guessed.append(letter)
    print(letters_guessed)
    print(blank)
    print("".join(blank))

    for i in range(len(word)):
        if word[i] in list(string.ascii_letters):
            blank.append('_')
        elif word[i] == ' ':
            blank.append(' ')
        elif word[i] == '.':
            blank.append('.')
        elif word[i] == '.':
            blank.append('.')

    for i in range(len(blank)):
        if letter in list(blank):
            blank.append(letter)

    if letter in word:
        blank.append(letter)
        print("".join(blank))
        print("Correct")
        print("You have %d guesses left." % guesses)
    elif letter in list(string.ascii_uppercase) and word:
        blank.append(letter)
        print("".join(blank))
        print("Correct")
        print("You have %d guesses left." % guesses)
    else:
        guesses -= 1
        print("Wrong")
        print("You have %d guesses left." % guesses)

    if letter == word:
        print("You guessed right, good job.")
        playing = False

    if guesses == 0:
        print("The word/phrase was '%s'" % word)
