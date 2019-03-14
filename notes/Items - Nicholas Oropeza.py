class Item(object):
    def __init__(self, name):
        self.name = name


class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)


class Weapon(Item):
    def __init__(self, name, damage_out, ammo):
        super(Weapon, self).__init__(name)
        self.damage_out = damage_out
        self.ammo = ammo


class Armor(Item):
    def __init__(self, name, damage_absorb):
        super(Armor, self).__init__(name)
        self.damage_absorb = damage_absorb


class Food(Consumable):
    def __init__(self, name, quantity, health_rec):
        super(Food, self).__init__(name)
        self.quantity = quantity
        self.health_recovered = health_rec


class Steak(Food):
    def __init__(self, name, quantity=None):
        super(Steak, self).__init__(name, quantity, 30)


class CookedRice(Food):
    def __init__(self, name):
        super(CookedRice, self).__init__(name, None, 20)


class Bread(Food):
    def __init__(self, name):
        super(Bread, self).__init__(name, None, 10)


class BronzeHelmet(Armor):
    def __init__(self, name):
        super(BronzeHelmet, self).__init__(name, 7)
        

class BronzeChestplate(Armor):
    def __init__(self, name):
        super(BronzeChestplate, self).__init__(name, 10)


class BronzeLeggings(Armor):
    def __init__(self, name):
        super(BronzeLeggings, self).__init__(name, 5)


class BronzeBoots(Armor):
    def __init__(self, name):
        super(BronzeBoots, self).__init__(name, 7)


class EnergyHelmet(Armor):
    def __init__(self, name):
        super(EnergyHelmet, self).__init__(name, 15)


class EnergyChestplate(Armor):
    def __init__(self, name):
        super(EnergyChestplate, self).__init__(name, 20)


class EnergyLeggings(Armor):
    def __init__(self, name):
        super(EnergyLeggings, self).__init__(name, 10)


class EnergyBoots(Armor):
    def __init__(self, name):
        super(EnergyBoots, self).__init__(name, 15)


class EnergySword(Weapon):
    def __init__(self, name):
        super(EnergySword, self).__init__(name, 10, None)


class EnergyDualies(Weapon):
    def __init__(self, name):
        super(EnergyDualies, self).__init__(name, 30, None)


class BronzeSword(Weapon):
    def __init__(self, name):
        super(BronzeSword, self).__init__(name, 5, None)


class RegularGun(Weapon):
    def __init__(self, name):
        super(RegularGun, self).__init__(name, 15, None)


class Character(object):
    def __init__(self, name, health: int, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.damage_absorb > damage:
            print("No damage is done because of some AMAZING armor.")
        else:
            self.health -= damage - self.armor.damage_absorb
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage_out))
        target.take_damage(self.weapon.damage_out)


sword = Weapon("Sword", 10, None)
canoe = Weapon("Canoe", 42, None)
wiebe_armor = Armor("Armor of the gods", 1000000000000000000)

# Characters
orc = Character("Orc1", 100, sword, BronzeChestplate)
orc2 = Character("Wiebe", 10000, canoe, wiebe_armor)

orc.attack(orc2)
orc2.attack(orc)
orc2.attack(orc)
orc2.attack(orc)
