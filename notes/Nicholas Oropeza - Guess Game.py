import random
random_number = random.randint(1, 10)
guesses_left = 4
playing = True
guess = (int(input("Enter a random number between 1 and 10: ")))

while guesses_left > 0 and playing and guess != random_number:
    if guess < random_number:
        print("Higher")
        guesses_left -= 1
        guess = (int(input("Go again: ")))
        print()
    else:
        print("Lower")
        guesses_left -= 1
        guess = (int(input("Go again: ")))
        print()

if guesses_left == 0 and playing:
    print("You lost")
    playing = False

if guess == random_number and playing:
    print("Good job you win")
    playing = False
