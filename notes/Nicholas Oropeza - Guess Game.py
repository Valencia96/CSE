import random
random_number = random.randint(1, 10)
guesses = 5
guess = (int(input("Enter a random number between 1 and 10")))

while guess != random_number and guesses > 0:
    if guess < random_number:
        print("Higher")
        guesses -= 1
        guess = (int(input("Go again")))
        print()
    else:
        print("Lower")
        guesses -= 1
        guess = (int(input("Go again")))
        print()

while guesses == 0:
    print("You lost")
    break

while guess == random_number:
    print("Good job you win")
    break
