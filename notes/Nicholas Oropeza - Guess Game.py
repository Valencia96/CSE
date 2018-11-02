import random
random_number = random.randint(1, 10)
guess = int(input("Enter a random number between 1 and 10"))
guesses = 5
while guess != random_number and guesses < 0:
    if guess < random_number:
        print("Higher")
    else:
        print("Lower")
