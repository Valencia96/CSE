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
        if random_choice == list(string.ascii_letters):  # if we find a letter
            random_choice(i)  # remove the i-th index
            random_choice.insert(i, "_")  # Put a _ there instead
   
    if letter != random_choice:
        print("Wrong, try again")
        guesses -= 1
    else:
        print("Good guess")
    if guesses == 0:
        print(random_choice)
