class Item(object):
    def __init__(self, name):
        self.name = name


class Consumable(Item):
    def __init__(self, name):
        super(Item, self).__init__(name)


class Armor(Item):
    def __init__(self, name, damage_absorb, durability):
        super(Item, self).__init__(name)
        self.damage_absorb = damage_absorb
        self.durability = durability


class Food(Consumable):
    def __init__(self, name, quantity, health_rec):
        super(Item, self).__init__(name)
        self.quantity = quantity
        self.health_recovered = health_rec

class Steak(Food):
    def __init__(self, name, quantity, consumed, health_rec):
        super(Steak, self).__init__(name, quantity, health_rec)
        self.consumed = False