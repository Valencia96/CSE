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
            cloth_profit += float(row[13])
        elif row[2] == 'Fruits':
            fruit_profit += float(row[13])
        elif row[2] == 'Meat':
            meat_profit += float(row[13])
        elif row[2] == 'Beverages':
            beverage_profit += float(row[13])
        elif row[2] == 'Office Supplies':
            office_profit += float(row[13])
        elif row[2] == 'Cosmetics':
            cosmetic_profit += float(row[13])
        elif row[2] == 'Snacks':
            snack_profit += float(row[13])
        elif row[2] == 'Personal Care':
            care_profit += float(row[13])
        elif row[2] == 'Household':
            house_profit += float(row[13])
        elif row[2] == 'Vegetables':
            vegetable_profit += float(row[13])
        elif row[2] == 'Baby Food':
            baby_profit += float(row[13])
        elif row[2] == 'Cereal':
            cereal_profit += float(row[13])

all_profits = [cloth_profit, fruit_profit, meat_profit, beverage_profit, office_profit, cosmetic_profit, snack_profit,
               care_profit, house_profit, vegetable_profit, baby_profit, cereal_profit]

print("The total amount of profits for clothes is: %d" % cloth_profit)
print("The total amount of profits for fruits is: %d" % fruit_profit)
print("The total amount of profits for meat is: %d" % meat_profit)
print("The total amount of profits for beverages is: %d" % beverage_profit)
print("The total amount of profits for office supplies is: %d" % office_profit)
print("The total amount of profits for cosmetics is: %d" % cosmetic_profit)
print("The total amount of profits for snacks is: %d" % snack_profit)
print("The total amount of profits for personal care products is: %d" % care_profit)
print("The total amount of profits for household items is: %d" % house_profit)
print("The total amount of profits for vegetables is: %d" % vegetable_profit)
print("The total amount of profits for baby food is: %d" % baby_profit)
print("The total amount of profits for cereal is: %d" % cereal_profit)
print()

if max(all_profits) == cloth_profit:
    print("Clothes are the most profitable items.")
if max(all_profits) == fruit_profit:
    print("Fruits are the most profitable items.")
if max(all_profits) == meat_profit:
    print("Meat is the most profitable item.")
if max(all_profits) == beverage_profit:
    print("Beverages are the most profitable items.")
if max(all_profits) == office_profit:
    print("Office Supplies are the most profitable items.")
if max(all_profits) == cosmetic_profit:
    print("Cosmetics are the most profitable items.")
if max(all_profits) == snack_profit:
    print("Snacks are the most profitable items.")
if max(all_profits) == care_profit:
    print("Personal Care Products are the most profitable items.")
if max(all_profits) == house_profit:
    print("Household items are the most profitable items.")
if max(all_profits) == vegetable_profit:
    print("Vegetables are the most profitable items.")
if max(all_profits) == baby_profit:
    print("Baby Food is the most profitable item.")
if max(all_profits) == cereal_profit:
    print("Cereal is the most profitable item.")

print("Done")
