import csv


def divisible_by_3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def digits_16(num: str):
    if len(num) == 16:
        return True
    else:
        print("NOT EVERY NUMBER IS 16 DIGITS")


def validate(num: str):
    if not digits_16(num):
        return False
    if divisible_by_2(num) and divisible_by_3(num):
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print("Writing New File...  ")
#         writer = csv.writer(new_csv)
#         reader = csv.reader(old_csv)
#         for row in reader:
#             old_number = row[0]
#             first_num = int(old_number[0])  # this is a string
#             if first_num % 2 == 0:
#                 writer.writerow(row)
#             # old_number = int(row[0] + 1)
#             # print(old_number)
# print("OK")
def reverse_it(string):
    print(string[::-1])


reverse_it("Hello World")


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        writer = csv.writer(new_csv)
        reader = csv.reader(old_csv)
        print("Processing...")
        for row in reader:
            # old_number = int(row[0]) + 1
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
print("Done")
