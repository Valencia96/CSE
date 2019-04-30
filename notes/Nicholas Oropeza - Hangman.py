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
print("Your word is a %d letter word" % len(word))
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
    print("".join(blank))
    letter = input("Enter the letter or word")

    for i in range(len(word)):
        if word.lower()[i] in letters_guessed:
            blank[i] = word[i]

    if letter.lower() in word.lower():
        print("Good guess!")
        letters_guessed.append(letter)
        print(letters_guessed)
    elif letter.lower() in letters_guessed:
        print("You already guessed that letter")
    else:
        guesses -= 1
        print("Wrong")
        print("You have %d guesses left." % guesses)

    if letter == word:
        print("You guessed right, good job.")
        playing = False

    if guesses == 0:
        print("The word/phrase was '%s'" % word)
