import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    subs_africa = 0
    mid_e_north_africa = 0
    australia = 0
    europe = 0
    asia = 0
    caribbean = 0
    n_america = 0
    print("Processing...")
    for row in reader:
        if row[0] == 'Sub-Saharan Africa':
            subs_africa += float(row[13])
        elif row[0] == 'Middle East and North Africa':
            mid_e_north_africa += float(row[13])
        elif row[0] == 'Australia and Oceania':
            australia += float(row[13])
        elif row[0] == 'Europe':
            europe += float(row[13])
        elif row[0] == 'Asia':
            asia += float(row[13])
        elif row[0] == 'Central America and the Caribbean':
            caribbean += float(row[13])
        elif row[0] == 'North America':
            n_america += float(row[13])

regions = [subs_africa, mid_e_north_africa, australia, europe, asia, caribbean, n_america]

print("The total amount of profits for Sub-Saharan Africa is: %d" % subs_africa)
print("The total amount of profits for the Middle East and North Africa is: %d" % mid_e_north_africa)
print("The total amount of profits for Australia and Oceania is: %d" % australia)
print("The total amount of profits for Europe is: %d" % europe)
print("The total amount of profits for Asia is: %d" % asia)
print("The total amount of profits for Central America and the Caribbean is: %d" % caribbean)
print("The total amount of profits for North America is: %d" % n_america)
print()

if max(regions) == subs_africa:
    print("Sub-Saharan Africa is the most profitable region.")
if max(regions) == mid_e_north_africa:
    print("The Middle East and North Africa is the most profitable region.")
if max(regions) == australia:
    print("Australia and Oceania is the most profitable region.")
if max(regions) == europe:
    print("Europe is the most profitable region.")
if max(regions) == asia:
    print("Asia is the most profitable region.")
if max(regions) == caribbean:
    print("Central America and the Caribbean is the most profitable region.")
if max(regions) == n_america:
    print("North America is the most profitable region.")
print("Done")
