class Mower(object):
    def __init__(self, gasoline=0, engine_oil=0):
        self.gas = gasoline
        self.safety = False
        self.cord = False
        self.oil = engine_oil
        self.clippings_bag = False

    def refill(self, liter):
        self.gas += liter
        self.oil += liter
        if self.gas > 15:
            print("WHAT ARE YOU DOING?")
            self.gas = 15
        if self.gas > 1:
            print("That's way too much oil.")
            self.oil = 1

    def run(self, duration, safety, cord, clippings):
        self.safety = safety
        self.cord = cord
        self.clippings_bag = clippings
        gas_loss_per_minute = 0.5
        oil_loss_per_minute = 0.01
        if not safety:
            print("Your safety hasn't been pulled.")
            return
        elif not cord:
            print("The cord wasn't pulled.")
            return
        elif not clippings:
            print("The grass bag wasn't attached.")
            return
        if self.gas <= 0:
            print("You don't have any gas in the tank.")
            print("Go refill the gas tank.")
            return
        elif self.oil <= 0:
            print("You don't have any oil in the tank.")
            print("Go refill the oil tank")
            return
        self.gas -= duration * gas_loss_per_minute
        self.oil -= duration * oil_loss_per_minute
        if self.gas < 0:
            self.gas = 0
            print("Your lawn mower runs out of gas before you finish mowing the lawn.")
        elif self.gas == 0:
            print("You run out of gas right after you mow the lawn.")
        else:
            print("You successfully mow the lawn.")
            print("You have %d liters of gas left" % self.gas)
        if self.oil < 0:
                self.oil = 0
                print("Your lawn mower runs out of oil before you finish mowing the lawn.")
        elif self.oil == 0:
            print("You run out of oil right after you mow the lawn.")
        else:
            print("You successfully mow the lawn.")
            print("You have %d liters of oil left." % self.oil)
            print()


my_mower = Mower(15, 1)
toro_mower = Mower(7, 1)

my_mower.run(30, True, True, True)
toro_mower.run(40, True, True, True)
