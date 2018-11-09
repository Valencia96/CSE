import random
money = int(15)
playing = True
d6_1 = random.randint(1, 6)
d6_2 = random.randint(1, 6)
roll = int(d6_1 + d6_2)
bet = (int(1))

print("You have %d Canadian Pesos" % money)
print()
print("You bet one Canadian Peso")
while money > 0 and playing:
    print(roll)
    print()
    if roll == 7:
        money == bet + 4
        print("You have %d Canadian Peso(s)" % money)
        print()
        print("You bet another Canadian Peso")
        print()
        roll = int(d6_1 + d6_2)
    else:
        money -= 1
        print("You have %d Canadian Peso(s)" % money)
        print()
        print("You bet another Canadian Peso")
        print()
        roll = int(d6_1 + d6_2)

while money == 0:
    playing = False
    print("You lost all of your money, loser.")
