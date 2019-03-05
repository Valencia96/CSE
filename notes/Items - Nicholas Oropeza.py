class Item(object):
    def __init__(self, name):
        self.name = name


class Consumable(Item):
    def __init__(self, name):
        super(Item, self).__init__(name)


class Weapon(Item):
    def __init__(self, name, damage_out, durability):
        super(Weapon, self).__init__(name)
        self.damage_out = damage_out
        self.durability = durability
        


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
    def __init__(self, name, quantity, health_rec, consumed=False):
        super(Steak, self).__init__(name, quantity, health_rec)
        self.consumed = consumed


class LeatherHelmet(Armor):
    def __init__(self, name, damage_absorb, durability, quantity):
        super(LeatherHelmet, self).__init__(name)
        self.quantity = quantity
        self.damage_absorb = damage_absorb
        self.durability = durability
        
        
class WoodenSword(Weapon):
    def __init__(self, name, ):
        super(WoodenSword, self).__init__(name)