import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    cloth_profit = 0
    fruit_profit = 0
    meat_profit = 0
    beverage_profit = 0
    office_profit = 0
    cosmetic_profit = 0
    snack_profit = 0
    care_profit = 0
    house_profit = 0
    vegetable_profit = 0
    baby_profit = 0
    cereal_profit = 0
    print("Processing...")
    for row in reader:
        if row[2] == 'Clothes':
            profits = float(row[13])
            for i in row[13]:
                cloth_profit += profits
        elif row[2] == 'Fruits':
            profits = float(row[13])
            for i in row[13]:
                fruit_profit += profits
        elif row[2] == 'Meat':
            profits = float(row[13])
            for i in row[13]:
                meat_profit += profits
        elif row[2] == 'Beverages':
            profits = float(row[13])
            for i in row[13]:
                beverage_profit += profits
        elif row[2] == 'Office Supplies':
            profits = float(row[13])
            for i in row[13]:
                office_profit += profits
        elif row[2] == 'Cosmetics':
            profits = float(row[13])
            for i in row[13]:
                cosmetic_profit += profits
        elif row[2] == 'Snacks':
            profits = float(row[13])
            for i in row[13]:
                snack_profit += profits
        elif row[2] == 'Personal Care':
            profits = float(row[13])
            for i in row[13]:
                care_profit += profits
        elif row[2] == 'Household':
            profits = float(row[13])
            for i in row[13]:
                house_profit += profits
        elif row[2] == 'Vegetables':
            profits = float(row[13])
            for i in row[13]:
                vegetable_profit += profits
        elif row[2] == 'Baby Food':
            profits = float(row[13])
            for i in row[13]:
                baby_profit += profits
        elif row[2] == 'Cereal':
            profits = float(row[13])
            for i in row[13]:
                cereal_profit += profits

print("The total amount of profits for clothes is: %d" % round(cloth_profit, 2))
print()
print("The total amount of profits for fruits is: %d" % round(fruit_profit, 2))
print()
print("The total amount of profits for meat is: %d" % round(meat_profit, 2))
print()
print("The total amount of profits for beverages is: %d" % round(beverage_profit, 2))
print()
print("The total amount of profits for office supplies is: %d" % round(office_profit, 2))
print()
print("The total amount of profits for cosmetics is: %d" % round(cosmetic_profit, 2))
print()
print("The total amount of profits for snacks is: %d" % round(snack_profit, 2))
print()
print("The total amount of profits for personal care is: %d" % round(care_profit, 2))
print()
print("The total amount of profits for household items is: %d" % round(house_profit, 2))
print()
print("The total amount of profits for vegetables is: %d" % round(vegetable_profit, 2))
print()
print("The total amount of profits for baby food is: %d" % round(baby_profit, 2))
print()
print("The total amount of profits for cereal is: %d" % round(cereal_profit, 2))
print("Done")
