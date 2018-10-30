"""
print("Hello World")

# This is a comment. This has no effect on the code
# but this does allow me to do things. I can:
# 1. Make notes to myself
# 2. Comment pieces of code that do not work
# 3. Make my code easier to read

print("Look at what happens here. Is there any space?")
print()
print()
print("There should be a couple of blank lines here.")
print()

print("Figure this out...")
print(6 // 2)
print(5 // 2)
print(9 // 4)

print("Here is another one...")
print(6 % 2)
print(5 % 2)
print(11 % 4)   # Modulus (Remainder)

print()
# Powers
# What is 2^20
print(2 ** 70)

# What is 2^100
print(2 ** 100)

# Taking input
name = input("What is your name?")
print("Hello %s." % name)

age = input("How old are you? >_")
print("%a?!? You belong in a museum." % age)
print()
print("%s is really old. They are %a years old." % (name, age))

# Variable Assignments
car_name = "my mom's car"
car_type = "Nissan Altima"
car_cylinders = 16
car_miles_per_gallon = 0.01

# Make it print "I have a car called my mom's car. It is a Nissan Altima.
print()
print("I have a car called %a. It is a %s." % (car_name, car_type))

# Recasting
real_age = int(input("How old are you again?"))
hidden_age = real_age + 5
print("This is your real age: %d" % hidden_age)
"""

"""
This is a multi-line comment
Anything between the "s is not run.
"""


# Functions
def say_it():
    print("Hello World!")


say_it()
say_it()
say_it()


def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)


def distance(x1, y1, x2, y2):
    dist = ((x2-x1) ** 2 + (y2-y1) ** 2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)


# Loops
for i in range(5):  # This gives the numbers 0 through 4
    say_it()

for i in range(8):
        print(1 + 1)

for i in range(5):
    f(1)

# While Loops
