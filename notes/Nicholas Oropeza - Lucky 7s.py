import random
money = int(15)
max_money = (money > 15)
playing = True
d6_1 = random.randint(1, 6)
d6_2 = random.randint(1, 6)
roll = d6_1 + d6_2
bet = (int(1))
turn = int(0)

print("You have %d Canadian Pesos" % money)
print()
print("You bet one Canadian Peso")
while money > 0 and playing:
    d6_1 = random.randint(1, 6)
    d6_2 = random.randint(1, 6)
    roll = d6_1 + d6_2
    print("You got a %d " % roll)
    print()
    turn += 1
    if roll == 7:
        money = money + bet + 4
        print("You have %d Canadian Peso(s)" % money)
        print()
        print("You bet another Canadian Peso")
        print()
    else:
        money -= 1
        print("You have %d Canadian Peso(s)" % money)
        print()
        print("You bet another Canadian Peso")
        print()

while money == 0 and playing:
    print("You lost all of your money, loser.")
    print("You lasted %d turns" % turn)
    print("You had the most money you had was %d pesos" % max_money)
    playing = False
