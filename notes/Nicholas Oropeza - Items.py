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
        self.quantity = quantity
        self.damage_absorb = damage_absorb


class Food(Consumable):
    def __init__(self, name, quantity, health_rec):
        super(Food, self).__init__(name)
        self.name = name
        self.quantity = quantity
        self.health_rec = health_rec


class Steak(Food):
    def __init__(self, name, quantity, health_rec):
        super(Steak, self).__init__(name, quantity, health_rec=30)
        self.name = "Steak"
        self.quantity = None
        self.health_rec = health_rec


class CookedRice(Food):
    def __init__(self, name, quantity, health_rec):
        super(CookedRice, self).__init__(name, quantity, health_rec=20)
        self.name = "Cooked Rice"
        self.quantity = None
        self.health_rec = health_rec


class Bread(Food):
    def __init__(self, name, quantity, health_rec):
        super(Bread, self).__init__(name, quantity, health_rec=10)
        self.name = "Bread"
        self.quantity = quantity
        self.health_rec = health_rec


class Potato(Food):
    def __init__(self, name, quantity, health_rec):
        super(Potato, self).__init__(name, quantity, health_rec=5)
        self.name = "Uncooked Potato"
        self.quantity = quantity
        self.health_rec = health_rec


class CookedPotato(Food):
    def __init__(self, name, quantity, health_rec):
        super(CookedPotato, self).__init__(name, quantity, health_rec=12)
        self.name = "Cooked Potato"
        self.quantity = quantity
        self.health_rec = health_rec


class BakedPotato(Food):
    def __init__(self, name, quantity, health_rec):
        super(BakedPotato, self).__init__(name, quantity, health_rec=15)
        self.name = "Baked Potato"
        self.quantity = quantity
        self.health_rec = health_rec


class Beans(Food):
    def __init__(self, name, quantity, health_rec):
        super(Beans, self).__init__(name, quantity, health_rec=1)
        self.name = "Uncooked Beans"
        self.quantity = quantity
        self.health_rec = health_rec


class BakedBeans(Food):
    def __init__(self, name, quantity, health_rec):
        super(BakedBeans, self).__init__(name, quantity, health_rec=15)
        self.name = "Baked Beans"
        self.quantity = quantity
        self.health_rec = health_rec


class Stew(Food):
    def __init__(self, name, quantity, health_rec):
        super(Stew, self).__init__(name, quantity, health_rec=20)
        self.name = "Stew"
        self.quantity = quantity
        self.health_rec = health_rec


class BronzeHelmet(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(BronzeHelmet, self).__init__(name, quantity, damage_absorb=7)
        self.name = "Bronze Helmet"
        self.quantity = quantity
        self.damage_absorb = damage_absorb


class BronzeChestplate(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(BronzeChestplate, self).__init__(name, quantity, damage_absorb=10)
        self.name = "Bronze Chestplate"
        self.quantity = quantity
        self.damage_absorb = damage_absorb


class BronzeLeggings(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(BronzeLeggings, self).__init__(name, quantity, damage_absorb=5)
        self.name = "Bronze Leggings"
        self.quantity = quantity
        self.damage_absorb = damage_absorb


class BronzeBoots(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(BronzeBoots, self).__init__(name, quantity, damage_absorb=7)
        self.name = "Bronze Boots"
        self.quantity = quantity
        self.damage_absorb = damage_absorb


class EnergyHelmet(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(EnergyHelmet, self).__init__(name, quantity, damage_absorb=15)
        self.name = "Energy Helmet"
        self.quantity = quantity
        self.damage_absorb = damage_absorb


class EnergyChestplate(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(EnergyChestplate, self).__init__(name, quantity, damage_absorb=20)
        self.name = "EnergyChestplate"
        self.quantity = quantity
        self.damage_absorb = damage_absorb


class EnergyLeggings(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(EnergyLeggings, self).__init__(name, quantity, damage_absorb=10)
        self.name = "Energy Leggings"
        self.quantity = quantity
        self.damage_absorb = damage_absorb


class EnergyBoots(Armor):
    def __init__(self, name, quantity, damage_absorb):
        super(EnergyBoots, self).__init__(name, quantity, damage_absorb=15)
        self.name = "Energy Boots"
        self.quantity = quantity
        self.damage_absorb = damage_absorb


class EnergySword(Weapon):
    def __init__(self, name, damage_out, ammo):
        super(EnergySword, self).__init__(name, damage_out=10, ammo=False)
        self.name = "Energy Sword"
        self.damage_out = damage_out
        self.ammo = ammo


class EnergyDualies(Weapon):
    def __init__(self, name, damage_out, ammo):
        super(EnergyDualies, self).__init__(name, damage_out=30, ammo=False)
        self.name = "Energy Dualies"
        self.damage_out = damage_out
        self.ammo = ammo


class BronzeSword(Weapon):
    def __init__(self, name, damage_out, ammo):
        super(BronzeSword, self).__init__(name, damage_out=5, ammo=False)
        self.name = "Bronze Sword"
        self.damage_out = damage_out
        self.ammo = ammo


class RegularGun(Weapon):
    def __init__(self, name, damage_out, ammo):
        super(RegularGun, self).__init__(name, damage_out=15, ammo=False)
        self.name = "Regular Gun"
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


sword = Weapon("Sword", 5, False)
canoe = Weapon("Canoe", 42, None)
wiebe_armor = Armor("Armor of the gods", 1, 4)

# Characters
orc = Character("Orc1", 100, sword, wiebe_armor)
orc2 = Character("Wiebe", 10000, canoe, wiebe_armor)

orc.attack(orc2)
orc2.attack(orc)
orc2.attack(orc)
