import csv

# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#       print("Writing New File...  ")
#        writer = csv.writer(new_csv)
#        reader = csv.reader(old_csv)
#        for row in reader:
#            old_number = int(row[0])
#            new_number = old_number + 1
#            row[0] = new_number
#            writer.writerow(row)
#            # old_number = int(row[0] + 1)
#            # print(old_number)
# print("OK")

with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing New File...  ")
        writer = csv.writer(new_csv)
        reader = csv.reader(old_csv)
        for row in reader:
            old_number = row[0]
            first_num = int(old_number[0])  # this is a string
            if first_num % 2 == 0:
                writer.writerow(row)
            # old_number = int(row[0] + 1)
            # print(old_number)
print("OK")
