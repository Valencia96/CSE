class Room(object):
    def __init__(self, name, desc, north=None, south=None, east=None, west=None, up=None, down=None, items=None):
        if items is None:
            items = []
        self.name = name
        self.desc = desc
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.characters = []


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
        self.damage_absorbed = damage_absorb


class Food(Consumable):
    def __init__(self, name, quantity, health_rec):
        super(Food, self).__init__(name)
        self.name = name
        self.quantity = quantity
        self.health_rec = health_rec


class Steak(Food):
    def __init__(self, name, quantity, health_rec):
        super(Steak, self).__init__(name, quantity, health_rec)
        self.name = "Steak"
        self.quantity = None
        self.health_rec = 30


class CookedRice(Food):
    def __init__(self, name, quantity, health_rec):
        super(CookedRice, self).__init__(name, quantity, health_rec)
        self.name = "Cooked Rice"
        self.quantity = None
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
        super(EnergyDualies, self).__init__(name, damage_out=30, ammo=False)
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
    def __init__(self, name, starting_location, health: int, weapon, armor):
        self.name = name
        self.current_location = starting_location
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


class Player(object):
    def __init__(self, name, health: int, weapon, starting_location, armor):
        self.name = name
        self.armor = armor
        self.current_location = starting_location
        self.health = health
        self.weapon = weapon
        self.inventory = []

    def move(self, new_location):
        """ This moves the player to a new room

        :param new_location: The room object of which you are going to.
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room so see if a room
        exists in that location.

        :param direction: The direction that you want to move to
        :return:   The Room object if it exists, or None if it does not
        """
        return getattr(self.current_location, direction)

    def battle_melee(self, target):
        print("You attack %s for %d damage with your %s" % (self.weapon.damage_out, target.name, self.weapon))
        target.take_damage(self.weapon.damage_out)

    def pick_up(self, target):
        print("You picked up %s and put it in your inventory." % )


closet = Room("Anton's Closet", "It's surprisingly empty")
anton_room = Room("Anton's Room", "A room that contains a bed, a desk, and a drawer.", items=[])
tunnel = Room("Dark Tunnel", "Dark, Dank Tunnel")
w_tunnel = Room("West Tunnel", "Dark, Dank Tunnel, but to the West")
skele_cave = Room("The Skeleton Cave", "There are at least 100 skeletons in here.")
end_tunnel = Room("The end of the tunnel.", "There is nothing beyond this point, go back.")
jaiden_room = Room("Jaiden's Room", "An unkempt room.")
stairs = Room("The staircase",
              "A staircase in between two rooms in the middle of the hallway.")
a_room = Room("A room", "An empty room with a bed in it.")
living_room = Room("The Living Room", "placeholder")
player_room = Room("Your Room", "The room is messy.")
kitchen = Room("The Kitchen", "The place where you cook stuff.")
b_room = Room("B room", "This room is empty.")
c_room = Room("C room", "This room is empty")

closet.west = anton_room
anton_room.east = closet
anton_room.down = tunnel
anton_room.north = jaiden_room
jaiden_room.west = stairs
jaiden_room.south = anton_room
a_room.east = stairs
b_room.west = living_room
c_room.east = living_room
stairs.east = jaiden_room
stairs.west = player_room
stairs.down = living_room
living_room.up = stairs
living_room.north = kitchen
living_room.east = b_room
living_room.west = c_room
tunnel.west = w_tunnel
tunnel.up = anton_room
w_tunnel.west = end_tunnel
w_tunnel.east = tunnel
end_tunnel.north = skele_cave
end_tunnel.east = w_tunnel

p_name = input("What is your name?")
player = Player(p_name, 100, None, closet, None)
character1 = Character("Arthur", closet, 100, None, None)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
overworld_actions = ['pick up', 'attack']
battle_actions = ['attack', 'items', 'run']

while playing:
    print(player.current_location.name)
    print(player.current_location.desc)
    command = input(">_")
    if command.lower in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            if next_room is None:
                raise AttributeError
            player.move(next_room)
        except AttributeError:
            print("There is nothing that way.")
            print()
        except KeyError:
            print("I can't go that way")

    else:
        print("Command Not Found")
