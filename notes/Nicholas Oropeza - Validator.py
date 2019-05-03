import csv
last_number = []


def multiply(num: str):
    num = int(num[0])
    if num % 2 == 0:
        return num * 2
    if num >= 10:
        return num - 9


def add_all(num: str):
    for index in range(len(num)):
        int(num) + int(num)
    return num % 10


def digits_16(num: str):
    if len(num) == 16:
        return True
    else:
        print("This number is not 16 digits long.")


def reverse_it(num: str):
    reversed_list = list(num[::-1])
    return reversed_list


def validate(num: str):
    for index in range(len(num)):
        num = int(num[index])
        return num
    last_number.append(num[15])
    if not digits_16(num):
        return False
    reverse_it(num)
    multiply(num)
    add_all(num)
    if num != last_number:
        print(num)


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