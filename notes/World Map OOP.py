class Room(object):
    def __init__(self, name, desc, north=None, south=None, east=None, west=None, up=None, down=None):
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
        super(Item, self).__init__(name)


class Weapon(Item):
    def __init__(self, name, damage_out, durability, ammo=None, equipped=False):
        super(Weapon, self).__init__(name)
        self.damage_out = damage_out
        self.durability = durability
        self.equipped = equipped
        self.ammo = ammo


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
    def __init__(self, name, consumed=False, quantity=None):
        super(Steak, self).__init__(name, quantity, 30)
        self.consumed = consumed


class CookedRice(Food):
    def __init__(self, name):
        super(CookedRice, self).__init__(name, None, 20)


class Bread(Food):
    def __init__(self, name):
        super(Bread, self).__init__(name, None, 10)


class BronzeHelmet(Armor):
    def __init__(self, name):
        super(BronzeHelmet, self).__init__(name, 7, 4)
        self.quantity = None


class BronzeChestplate(Armor):
    def __init__(self, name):
        super(BronzeChestplate, self).__init__(name, 3, 5)
        self.quantity = None


class BronzeLeggings(Armor):
    def __init__(self, name):
        super(BronzeLeggings, self).__init__(name, 5, 5)


class BronzeBoots(Armor):
    def __init__(self, name):
        super(BronzeBoots, self).__init__(name, 3, 5)
        self.quantity = None


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
        super(EnergySword, self).__init__(name, 10, 10)


class EnergyDualies(Weapon):
    def __init__(self, name):
        super(EnergyDualies, self).__init__(name, 30, 1000)


class BronzeSword(Weapon):
    def __init__(self, name):
        super(BronzeSword, self).__init__(name, 5, 5)


class RegularGun(Weapon):
    def __init__(self, name):
        super(RegularGun, self).__init__(name, 15, 500)


class Character(object):
    def __init__(self, name, starting_location):
        self.name = name
        self.current_location = starting_location


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
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


closet = Room("Anton's Closet", "There are a lot of clothes in here")
anton_room = Room("Anton's Room", "A room that contains a bed, a desk, and a drawer.")
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


player = Player(closet)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

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
