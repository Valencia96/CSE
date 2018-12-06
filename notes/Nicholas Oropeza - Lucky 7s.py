import random
"The is a gambling game in where you can't win and where the money isn't real, "
"called 'Lucky 7s'"

money = int(15)  # The amount of money you start with
max_money = int(15)  # The most amount of money you've had
max_roll = int(0)  # The roll on which you had the most money
playing = True
bet = 1  # The amount of money you have bet
turn = int(0)  # The turn number


print("Turn: %d" % turn)  # The current turn number
print("You have %d Canadian Pesos" % money)  # The amount of money you currently have
print("You bet one Canadian Peso")  # Note, the Canadian peso is not the real currency of Canada

while money > 0 and playing:
    d6_1 = random.randint(1, 6)  # The dice 'roll' is stated again to re-roll the dice
    d6_2 = random.randint(1, 6)
    roll = (d6_1 + d6_2)  # This just adds the dice rolls each turn
    print()
    print("You got a %d " % roll)
    print()
    turn += 1  # Adds one to the turn counter
    if max_money < money:
        max_money = money
        max_roll = roll
    # Each time you get a 7 you win 5 pesos
    if roll == 7:
        money += 4
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

if money == 0 and playing:
    if max_roll == 0:
        print("You shouldn't have come here.")  # As in you were really unlucky
print()
print("You lasted %d turns" % turn)
print("You had the most money you had was %d pesos" % max_money)
print("You should have stopped on roll %d " % max_roll)
print("You lost all of your money, loser.")
playing = False
