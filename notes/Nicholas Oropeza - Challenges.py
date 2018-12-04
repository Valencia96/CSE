# Easy Challenges
def challenge1(first_name, last_name):
    return last_name, first_name


print(challenge1("Nico", "Oropeza"))


def challenge2(numb):
    if numb % 2 == 0:
        return "This is an even number"
    elif numb % 2 == 1:
        return "This is an odd number"


print(challenge2(-2))


def challenge3(a, b):
    return (a**2 + b**2)**(1/2)


print(challenge3(3, 4))


def challenge4(number):
    if number < 0:
        return number, 'is Negative'
    elif number > 0:
        return number, 'is Positive'
    else:
        return number, 'is Zero'


print(challenge4(0))


# Medium Challenges
def challenge5(r):
    return 3.14 * r ** 2


print(challenge5(2))


def challenge6(radius):
    return 4/3 * (3.14 * radius**3)


print(challenge6(2))


def challenge7(n):
    int(n)
    return n + n * n + n * n * n


print(challenge7(6))

