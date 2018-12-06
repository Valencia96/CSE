# Easy Challenges
def challenge1(first_name, last_name):
    return last_name, first_name


print(challenge1("Nico", "Oropeza"))


def challenge2(n):
    if n % 2 == 0:
        return "This is an even number"
    else:
        return "This is an odd number"


print(challenge2(-2))


def challenge3(a, b):
    return (a**2 + b**2)**(1/2)


print(challenge3(3, 4))


def challenge4(n):
    if n < 0:
        return n, 'is Negative'
    elif n > 0:
        return n, 'is Positive'
    else:
        return n, 'is Zero'


print(challenge4(0))


# Medium Challenges
def challenge5(radius):
    return 3.14 * radius ** 2


print(challenge5(2))


def challenge6(radius):
    return 4/3 * (3.14 * radius**3)


print(challenge6(2))


def challenge7(n):
    return n + n * n + n * n * n


print(challenge7(6))


def challenge8(n):
    if n >= 1850:
        return "In range"
    elif n > 2150:
        return "Not in range"
    elif n >= 2850:
        return "In range"
    elif n > 3150:
        return "Not in range"


print(challenge8(1840))


def challenge9(ch):
    if (ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch=='I'
     or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch =='u'):
        return "This letter is a vowel"
    else:
        return "This isn't a vowel"


print(challenge9("b"))
