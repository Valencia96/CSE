# The Luhn Formula:
#
# Drop the last digit from the number. The last digit is what we want to check against
# Reverse the numbers
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you would need to add to get a multiple
# of 10 (Modulo 10)
last_number = []


def digits_16(num: str):
    if len(num) == 16:
        return False
    else:
        return num


def reverse_it(num: str):
    reversed_list = list(num[::-1])
    return reversed_list


def divisible_by_2(num: str):
    num = int(num[0])
    if num % 2 == 0:
        return num * 2


def modulo10(num: int):
    if num >= 10:
        return num - 9


def add_all(num: str):
    for index in range(len(num)):
        sum(num)
    modulo10(int(num))


def validate(num: str):
    last_number.append(num[15])
    digits_16(num)
    reverse_it(num)
    int(num) / 10
    for index in range(len(num)):
        num = int(num[index])
        return num
    divisible_by_2(num)

    add_all(num)
    if num != last_number:
        print(num)
    return False


print(validate("9311368868957020"))
print(last_number)
# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile2.csv", 'w', newline='') as new_csv:
#         writer = csv.writer(new_csv)
#         reader = csv.reader(old_csv)
#         print("Processing...")
#         for row in reader:
#             old_number = row[0]
#             if validate(old_number):
#                 writer.writerow(row)
# print("Done")
