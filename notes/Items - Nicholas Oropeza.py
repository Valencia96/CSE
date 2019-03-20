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
    def __init__(self, name, quantity, damage_absorb):
        super(Armor, self).__init__(name)
        self.name = name
        self.quantity = quantity
        self.damage_absorbed = damage_absorb


class Food(Consumable):
    def __init__(self, name, quantity, health_rec):
        super(Food, self).__init__(name)
        self.quantity = quantity
        self.health_recovered = health_rec


class Steak(Food):
    def __init__(self, name, quantity, health_rec):
        super(Steak, self).__init__(name, None, 30)
        self.name = name
        self.quantity = quantity
        self.health_recovered = health_rec


class CookedRice(Food):
    def __init__(self, name, quantity, health_rec):
        super(CookedRice, self).__init__(name, None, 20)
        self.name = name
        self.quantity = quantity
        self.health_recovered = health_rec


class Bread(Food):
    def __init__(self, name, quantity, health_rec):
        super(Bread, self).__init__(name, None, 10)
        self.name = name
        self.quantity = quantity
        self.health_recovered = health_rec


class BronzeHelmet(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(BronzeHelmet, self).__init__(name, None, 7)
        self.name = name
        self.quantity = quantity
        self.damage_absorbed = damage_absorb


class BronzeChestplate(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(BronzeChestplate, self).__init__(name, None, 10)
        self.name = name
        self.quantity = quantity
        self.damage_absorbed = damage_absorb


class BronzeLeggings(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(BronzeLeggings, self).__init__(name, None, 5)
        self.name = name
        self.quantity = quantity
        self.damage_absorbed = damage_absorb


class BronzeBoots(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(BronzeBoots, self).__init__(name, None, 7)
        self.name = name
        self.quantity = quantity
        self.damage_absorbed = damage_absorb


class EnergyHelmet(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(EnergyHelmet, self).__init__(name, None, 15)
        self.name = name
        self.quantity = quantity
        self.damage_absorbed = damage_absorb


class EnergyChestplate(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(EnergyChestplate, self).__init__(name, None, 20)
        self.name = name
        self.quantity = quantity
        self.damage_absorbed = damage_absorb


class EnergyLeggings(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(EnergyLeggings, self).__init__(name, None, 10)
        self.name = name
        self.quantity = quantity
        self.damage_absorbed = damage_absorb


class EnergyBoots(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(EnergyBoots, self).__init__(name, None, 15)
        self.name = name
        self.quantity = quantity
        self.damage_absorbed = damage_absorb


class EnergySword(Weapon):
    def __init__(self, name, damage_out, ammo):
        super(EnergySword, self).__init__(name, 10, False)
        self.name = name
        self.damage_out = damage_out
        self.ammo = ammo


class EnergyDualies(Weapon):
    def __init__(self, name, damage_out, ammo):
        super(EnergyDualies, self).__init__(name, 30, False)
        self.name = name
        self.damage_out = damage_out
        self.ammo = ammo


class BronzeSword(Weapon):
    def __init__(self, name, damage_out, ammo):
        super(BronzeSword, self).__init__(name, damage_out, ammo)
        self.name = name
        self.damage_out = damage_out
        self.ammo = ammo


class RegularGun(Weapon):
    def __init__(self, name, damage_out, ammo):
        super(RegularGun, self).__init__(name, 15, False)
        self.name = name
        self.damage_out = damage_out
        self.ammo = ammo


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


sword = BronzeSword("Sword", 5, False)
canoe = Weapon("Canoe", 42, None)
wiebe_armor = Armor("Armor of the gods", 1, 4)

# Characters
orc = Character("Orc1", 100, sword, wiebe_armor)
orc2 = Character("Wiebe", 10000, canoe, wiebe_armor)

orc.attack(orc2)
orc2.attack(orc)
orc2.attack(orc)
