class Mower(object):
    def __init__(self, gasoline=0, engine_oil=0):
        self.gas = gasoline
        self.safety = False
        self.cord = False
        self.oil = engine_oil
        self.clippings_bag = False

    def refill(self, liter):
        self.gas += liter
        if self.gas > 15:
            print("WHAT ARE YOU DOING?")
            self.gas = 15

    def run(self, duration):
        if not self.safety:
            print("You can't turn it on, you haven't pulled the lever down.")
            return
        if not self.clippings_bag:
            print("You can't mow the lawn without the clippings bag.")
            return
        if not self.cord:
            print("You haven't pulled the cord.")
            print("How are you supposed to start the lawn mower pulling it?")
        gas_loss_per_minute = 1
        if self.gas <= 0:
            print("You don't have any gas in the tank.")
            print("Go refill the gas tank.")
            return
        self.gas -= duration * gas_loss_per_minute
        if self.gas < 0:
            self.gas = 0
            print("Your lawn mower dies before you finish")
        elif self.gas == 0:
            print("You successfully mow the lawn.")
