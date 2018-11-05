import random
random_number = random.randint(1, 10)
guesses = 5


def guess():
    int(input("Enter a random number between 1 and 10"))


def start():
    guess()


while guess != random_number and guesses > 0:
    if guess < random_number:
        print("Higher")
        guesses -= 1
        start()
    else:
        print("Lower")
        guesses -= 1
        start()
