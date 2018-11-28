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
print()
print(countries[1:4])
print()
print(countries[1:])
print()
print(countries[:4])

food_list = ["Pozole", "Sushi", "Steak", "Tamales", "Enchiladas", "Tacos" "Beans", "Instant Noodles", "Chicken",
             "Canadian Bacon", "Oreo", "Mexican Rice", "Hot Wings", "Hot Dogs", "Calzone", "Chicken Alfredo", "Salad",
             "Pizza", "Carne Asada", "Waffles"]

print()

# Adding stuff to a list
food_list.append("Bacon")
food_list.append("Eggs")
# Notice that everything is object.method(parameters)
print(food_list)
print()

food_list.insert(1, "Eggo Waffles")
print(food_list)
print()

# Removing things from list
food_list.remove("Salad")
print(food_list)
print()

"""
1. Make a new list with 3 items
2. Add a 4th item to the list
3. Remove one of the fist three items from the list
"""

# Tuples
brands = ("Apple", "Samsung", "HTC")  # Notice the parenthesis
new_list = ["Kirby", "Mario", "Link"]
print(new_list)

new_list.append("Pikachu")
new_list.append("Yoshi")
new_list.remove("Mario")
print(new_list)
print()

# Also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)

# Find the index of an item
print(food_list.index("Chicken"))

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

# Hangman hints
for i in range(len(list1)):  # i goes through all indices
    if list1[1] == "u":  # if we find a U
        list1.pop(i)  # remove the i-th index
        list1.insert(i, "*")  # Put a * there instead
'''
for character in list1:
    if character == "u"
        current_index = list1.index(characters)
        list1.pop(current_index)
        list1.insert(current_index, "*")
'''
# Turn a list into a string
print("".join(list1))
