import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    total_profit = 0
    print("Processing...")
    for row in reader:
        if row[2] == 'Clothes':
            profits = row[13]
            sum(float(profits))
print("Done")
print(total_profit)
