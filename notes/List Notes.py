# Creating a list
colors = ["blue", "turquoise", "pink", "orange", "black",
          "red", "cyan", "brown", "magenta"]  # USE SQUARE BRACKETS!!!!!
print()
print(colors)
print()
print(colors[1])
print()
print(colors[0])
print()

# Length of the list
print("There are %d things in the list." % len(colors))

# Changing Elements in a list
colors[1] = "green"
print(colors)
print()

# Looping through lists
for item in colors:
    print(item)

print()

'''
1. Make a list
2. Change the 3rd thing in the list
3. Print the item
4. Print the full list
'''

countries = ["United States", "Canada", "Mexico", "Panama", "Haiti",
             "Jamaica", "Peru"]

countries[2] = "the UK"
print(countries[2])
print()
print(countries)
print()
print("The last thing in the list is %s" % countries[len(countries) - 1])
print()

# Slicing a list
print(countries[1:3])
print(countries[1:4])
print(countries[1:])
print(countries[:4])
