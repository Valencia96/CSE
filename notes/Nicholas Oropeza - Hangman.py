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
random_choice = random.choice(word_bank)
letters_guessed = []
guesses = 8
playing = True

while guesses > 0 and playing:
    letter = input("Enter the letter or word")
    letters_guessed.append(letter)
    print(letters_guessed)
    
    for i in range(len(random_choice)):  # i goes through all indices
        if random_choice[i] in list(string.ascii_letters):  # if we find a letter
            letters_guessed.append(random_choice)
        elif random_choice[i]:

    print("".join(random_choice))

    if letter != random_choice:
        print("Wrong, try again")
        guesses -= 1
        print("You have %d guesses left" % guesses)
        print()

    if letter == random_choice:
        print("You win!")
        playing = False

    if guesses == 0:
        print("The word was '%s'" % random_choice)
