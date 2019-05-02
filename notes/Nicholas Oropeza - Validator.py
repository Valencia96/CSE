import csv
# Drop the last digit from the number. The last digit is what we want to check against
# Reverse the numbers
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10(Mod 10)
last_number = []


def multiply(num: str):
    num = int(num[0])
    if num % 2 == 0:
        return num * 2
    if num >= 10:
        return num - 9


def digits_16(num: str):
    if len(num) == 16:
        return True
    else:
        print("This number is not 16 digits long.")


def reverse_it(num: str):
    reversed_list = list(num[::-1])
    print(reversed_list)


def validate(num: str):
    for index in range(len(num)):
        num[index] = int(num[index])
        return num
    last_number.append(num[15])
    if not digits_16(num):
        return False
    reverse_it(num)
    multiply(num)


print(validate("Book1.csv"))


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
