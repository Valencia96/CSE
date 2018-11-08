import random
money = int(15)
playing = True
d6_1 = random.randint(1, 6)
d6_2 = random.randint(1, 6)
added_dice = int(d6_1 + d6_2)
bet = (int(1))

print()
print("You bet %d Canadian Peso(s)" % bet)
while money > 0 and playing:
    print 1 (added_dice)
    print()
if added_dice == 7:
    money -= 1
    print("You have %d Canadian Peso(s)" % money)
    print("You bet another Canadian Peso")
    print()
else:
    money == bet + 4
    print("You have %d Canadian Peso(s)" % money)
    print()
    print("You bet another Canadian Peso")
    print()
    money -= 1

while money == 0:
    playing = False
    print("You lost all of your money, loser.")
