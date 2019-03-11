class Item(object):
    def __init__(self, name):
        self.name = name


class Consumable(Item):
    def __init__(self, name):
        super(Item, self).__init__(name)


class Weapon(Item):
    def __init__(self, name, damage_out, durability, equipped=False):
        super(Weapon, self).__init__(name)
        self.damage_out = damage_out
        self.durability = durability
        self.equipped = equipped


class Armor(Item):
    def __init__(self, name, damage_absorb, durability, equipped=False):
        super(Item, self).__init__(name)
        self.damage_absorb = damage_absorb
        self.durability = durability
        self.equipped = equipped


class Food(Consumable):
    def __init__(self, name, quantity, health_rec, consumed=False):
        super(Item, self).__init__(name)
        self.quantity = quantity
        self.health_recovered = health_rec
        self.consumed = consumed


class Steak(Food):
    def __init__(self, name, consumed=False):
        super(Steak, self).__init__(name, quantity, health_rec=10)
        self.consumed = consumed
        self.health_rec = health_rec
        self.quantity = quantity


class BronzeHelmet(Armor):
    def __init__(self, name, damage_absorb=3):
        super(BronzeHelmet, self).__init__(name, quantity, durability=4)
        self.quantity = quantity
        self.damage_absorb = damage_absorb
        self.durability = durability
        

class BronzeChestplate(Armor):
    def __init__(self, name):
        super(BronzeChestplate, self).__init__(name, 3, 5)
        self.quantity = quantity
        self.damage_absorb = damage_absorb
        self.durability = durability


class BronzeLeggings(Armor):
    def __init__(self, name):
        super(BronzeLeggings, self).__init__(name, damage_absorb=5, durability=5)


class BronzeBoots(Armor):
    def __init__(self, name):
        super(BronzeBoots, self).__init__(name, 3, 5)
        self.quantity = quantity
        self.damage_absorb = damage_absorb
        self.durability = durability


class EnergyHelmet(Armor):
    def __init__(self, name):
        super(EnergyHelmet, self).__init__(name, 15, 200)


class EnergyChestplate(Armor):
    def __init__(self, name):
        super(EnergyChestplate, self).__init__(name, 20, 200)


class EnergyLeggings(Armor):
    def __init__(self, name):
        super(EnergyLeggings, self).__init__(name, 10, 200)


class EnergyBoots(Armor):
    def __init__(self, name):
        super(EnergyBoots, self).__init__(name, 15, 200)


class EnergySword(Weapon):
    def __init__(self, name):
        super(EnergySword, self).__init__(name, damage_out=10, durability=10)


class EnergyDualies(Weapon):
    def __init__(self, name):
        super(EnergyDualies, self).__init__(name, 30, 1000, False)


class BronzeSword(Weapon):
    def __init__(self, name):
        super(BronzeSword, self).__init__(name, 5, 5)


# three more items
