import csv


def row(string):
    if string == "Vietnam":



with open("Sales Records.csv", 'r') as old_csv:
    with open("Test.csv", 'w', newline='') as new_csv:
        writer = csv.writer(new_csv)
        reader = csv.reader(old_csv)
        print("Processing...")
        for row in reader:
            # old_number = int(row[0]) + 1
            old_number = row[0]
            writer.writerow(row)
print("Done")
