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
            profits = float(row[13])
            for i in row[13]:
                subs_africa += profits
        elif row[0] == 'Middle East and North Africa':
            profits = float(row[13])
            for i in row[13]:
                mid_e_north_africa += profits
        elif row[0] == 'Australia and Oceania':
            profits = float(row[13])
            for i in row[13]:
                australia += profits
        elif row[0] == 'Europe':
            europe = float(row[13])
            for i in row[13]:
                subs_africa += profits
        elif row[0] == 'Asia':
            profits = float(row[13])
            for i in row[13]:
                asia += profits
        elif row[0] == 'Central America and the Caribbean':
            profits = float(row[13])
            for i in row[13]:
                subs_africa += profits
        elif row[0] == 'North America':
            profits = float(row[13])
            for i in row[13]:
                n_america += profits


print("The total amount of profits for Sub-Saharan Africa is: %d" % subs_africa)
