import csv

cloth_profit = int(0)

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")
    for row in reader:
        if row[2] == 'Clothes':
            profits = float(row[13])
            cloth_profit += profits

print("The total amount of profits for clothes is: %d" % round(cloth_profit, 2))
print("Done")
