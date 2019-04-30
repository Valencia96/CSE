import csv


def digits_16(num: str):
    if len(num) == 16:
        return True
    else:
        print("This number is not a 16 digits long.")


def reverse_it(num: str):
    reversed_list = list(num[::-1])
    print(reversed_list)


list_num = list("7820959846382680")


for i in range(len(list_num)):
    list_num[i] = int(list_num[i])
    print(list_num)


def validate(num: str):
    if not digits_16(num):
        return False
    reverse_it(num)


# print(validate("7820959846382680"))

with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile2.csv", 'w', newline='') as new_csv:
        writer = csv.writer(new_csv)
        reader = csv.reader(old_csv)
        print("Processing...")
        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
print("Done")
