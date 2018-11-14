import random
money = int(15)
max_money = int(15)
max_roll = int(0)
playing = True
d6_1 = random.randint(1, 6)
d6_2 = random.randint(1, 6)
roll = d6_1 + d6_2
bet = (int(1))
turn = int(0)


print("Turn: %d" % turn)
print("You have %d Canadian Pesos" % money)
print("You bet one Canadian Peso")
while money > 0 and playing:
    d6_1 = random.randint(1, 6)
    d6_2 = random.randint(1, 6)
    roll = d6_1 + d6_2
    print()
    print("You got a %d " % roll)
    print()
    turn += 1
    if max_money < money:
        max_money = money
        max_roll = roll
    if roll == 7:
        money = money + bet + 4
        print("Turn: %d" % turn)
        print("You have %d Canadian Peso(s)" % money)
        print("You bet another Canadian Peso")
        print()
    else:
        money -= 1
        print("Turn: %d" % turn)
        print("You have %d Canadian Peso(s)" % money)
        print("You bet another Canadian Peso")
        print()

while money == 0 and playing:
    if max_roll == 0:
        print("You shouldn't have come here.")
    print()
    print("You lasted %d turns" % turn)
    print("You had the most money you had was %d pesos" % max_money)
    print("You should have stopped on roll %d " % max_roll)
    print("You lost all of your money, loser.")
    playing = False
