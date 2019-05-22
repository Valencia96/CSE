# Note, not final submission/ product


class Room(object):
    def __init__(self, name, desc, north=None, south=None, east=None, west=None, up=None, down=None, items=None,
                 characters=None, enemies=None):
        if enemies is None:
            enemies = []
        if characters is None:
            characters = []
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
        self.items = items
        self.characters = characters
        self.enemies = enemies


class Item(object):
    def __init__(self, name, desc):
        self.name = name
        self.description = desc


class Consumable(Item):
    def __init__(self, name, desc):
        super(Consumable, self).__init__(name, desc)


class Weapon(Item):
    def __init__(self, name, desc, damage_out, ammo):
        super(Weapon, self).__init__(name, desc)
        self.damage_out = damage_out
        self.ammo = ammo
        self.description = desc


class Armor(Item):
    def __init__(self, name, desc, quantity, damage_absorb):
        super(Armor, self).__init__(name, desc)
        self.quantity = quantity
        self.damage_absorb = damage_absorb
        self.description = desc


class Food(Consumable):
    def __init__(self, name, desc, quantity, health_rec):
        super(Food, self).__init__(name, desc)
        self.name = name
        self.quantity = quantity
        self.health_rec = health_rec
        self.description = desc


class Steak(Food):
    def __init__(self, name, desc, quantity, health_rec):
        super(Steak, self).__init__(name, desc, quantity, health_rec=30)
        self.name = "Steak"
        self.quantity = None
        self.health_rec = health_rec
        self.description = desc


class CookedRice(Food):
    def __init__(self, name, desc, quantity, health_rec):
        super(CookedRice, self).__init__(name, desc, quantity, health_rec=20)
        self.name = "Cooked Rice"
        self.quantity = None
        self.health_rec = health_rec
        self.description = desc


class Bread(Food):
    def __init__(self, name, desc, quantity, health_rec):
        super(Bread, self).__init__(name, desc, quantity, health_rec=10)
        self.name = "Bread"
        self.quantity = quantity
        self.health_rec = health_rec
        self.description = desc


class Potato(Food):
    def __init__(self, name, desc, quantity, health_rec):
        super(Potato, self).__init__(name, desc, quantity, health_rec=5)
        self.name = "Uncooked Potato"
        self.quantity = quantity
        self.health_rec = health_rec
        self.description = desc


class CookedPotato(Food):
    def __init__(self, name, desc, quantity, health_rec):
        super(CookedPotato, self).__init__(name, desc, quantity, health_rec=12)
        self.name = "Cooked Potato"
        self.quantity = quantity
        self.health_rec = health_rec
        self.description = desc


class BakedPotato(Food):
    def __init__(self, name, desc, quantity, health_rec):
        super(BakedPotato, self).__init__(name, desc, quantity, health_rec)
        self.name = "Baked Potato"
        self.quantity = quantity
        self.health_rec = 15
        self.description = desc


class Beans(Food):
    def __init__(self, name, desc, quantity, health_rec):
        super(Beans, self).__init__(name, desc, quantity, health_rec=1)
        self.name = "Uncooked Beans"
        self.quantity = quantity
        self.health_rec = health_rec
        self.description = desc


class BakedBeans(Food):
    def __init__(self, name, desc, quantity, health_rec):
        super(BakedBeans, self).__init__(name, desc, quantity, health_rec=15)
        self.name = "Baked Beans"
        self.quantity = quantity
        self.health_rec = health_rec
        self.description = desc


class Stew(Food):
    def __init__(self, name, desc, quantity, health_rec):
        super(Stew, self).__init__(name, desc, quantity, health_rec=20)
        self.name = "Stew"
        self.quantity = quantity
        self.health_rec = health_rec
        self.description = desc


class SpicyPepper(Food):
    def __init__(self, name, desc, quantity, health_rec):
        super(SpicyPepper, self).__init__(name, desc, quantity, health_rec=5)
        self.name = "Spicy Pepper"
        self.quantity = quantity
        self.health_rec = health_rec
        self.description = desc


class BronzeHelmet(Armor):
    def __init__(self, name, desc, quantity, damage_absorb):
        super(BronzeHelmet, self).__init__(name, desc, quantity, damage_absorb=7)
        self.name = name
        self.name = "Bronze Helmet"
        self.quantity = quantity
        self.damage_absorb = damage_absorb
        self.description = desc


class BronzeChestplate(Armor):
    def __init__(self, name, desc, quantity, damage_absorb):
        super(BronzeChestplate, self).__init__(name, desc, quantity, damage_absorb=10)
        self.name = name
        self.name = "Bronze Chestplate"
        self.quantity = quantity
        self.damage_absorb = damage_absorb
        self.description = desc


class BronzeLeggings(Armor):
    def __init__(self, name, desc, quantity, damage_absorb):
        super(BronzeLeggings, self).__init__(name, desc, quantity, damage_absorb=5)
        self.name = name
        self.name = "Bronze Leggings"
        self.quantity = quantity
        self.damage_absorb = damage_absorb
        self.description = desc


class BronzeBoots(Armor):
    def __init__(self, name, desc, quantity, damage_absorb):
        super(BronzeBoots, self).__init__(name, desc, quantity, damage_absorb=7)
        self.name = name
        self.name = "Bronze Boots"
        self.quantity = quantity
        self.damage_absorb = damage_absorb
        self.description = desc


class BronzeSword(Weapon):
    def __init__(self, name, damage_out, ammo, desc):
        super(BronzeSword, self).__init__(name, desc, damage_out=5, ammo=False)
        self.name = name
        self.name = "Bronze Sword"
        self.damage_out = damage_out
        self.ammo = ammo
        self.description = desc


class RegularGun(Weapon):
    def __init__(self, name, damage_out, ammo, desc):
        super(RegularGun, self).__init__(name, desc, damage_out=15, ammo=False)
        self.name = name
        self.name = "Regular Gun"
        self.damage_out = damage_out
        self.ammo = ammo
        self.description = desc


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
        print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage." % (self.name, target.name, self.weapon.damage_out))
        target.take_damage(self.weapon.damage_out)


class Enemy(Character):
    def __init__(self, name, starting_location, health: int, weapon, armor):
        super(Enemy, self).__init__(name, starting_location, health, weapon, armor)
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
        print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage." % (self.name, target.name, self.weapon.damage_out))
        target.take_damage(self.weapon.damage_out)


class Player(object):
    def __init__(self, name, health: int, weapon, starting_location, armor, inventory=None):
        if inventory is None:
            inventory = []
        self.name = name
        self.armor = armor
        self.current_location = starting_location
        self.health = health
        self.weapon = weapon
        self.inventory = inventory

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

    def attack(self, target):
        """

        :param target: The target (your opponent(s))
        :return:    The damage output of your weapon, the name of the target, the name of your weapon.
                    How much damage your opponent(s) took.
        """
        print("You attack %s for %d damage with your %s." % (target.name, self.weapon.damage_out, self.weapon))
        target.take_damage(self.weapon.damage_out)


tunnel = Room("Dark Tunnel", "Dark, Dank Tunnel")
w_tunnel = Room("West Tunnel", "Dark, Dank Tunnel, but to the West")
skele_cave = Room("The Skeleton Cave", "There are at least 100 skeletons in here.")
end_tunnel = Room("The end of the tunnel.", "There is nothing beyond this point, go back.")
stairs = Room("The staircase",
              "A staircase in between two rooms in the middle of the hallway.")
a_room = Room("A room", "An empty room with a bed in it.")
living_room = Room("The Living Room", "placeholder")
player_room = Room("Your Room", "The room is messy.")
kitchen = Room("The Kitchen", "The place where you cook stuff.")
b_room = Room("B room", "This room is empty.")
c_room = Room("C room", "This room is empty")

bronze_sword = BronzeSword("Bronze Sword", 15, None, "A sword made of bronze.")
fists = BronzeSword("Fists", 1, None, "Your fists.")
bronze_chestplate = BronzeChestplate("Bronze Chestplate", "A chestplate made of bronze.", 1, 10)
baked_potato = BakedPotato("Baked Potato", "A delicious potato smothered in butter.", 1, 5)
bread = Bread("Bread", "A loaf of bread that smells fresh from the oven.", 1, 10)

player = Player("Kagero", 100, fists, tunnel, None)
character1 = Character("Placeholder", None, 10, None, None)
goblin = Enemy("Goblin", None, 10, bronze_sword, bronze_chestplate)

player.inventory = []
tunnel.items = [baked_potato, bronze_chestplate]
w_tunnel.items = [baked_potato, bread]
tunnel.enemies = [goblin]
tunnel.characters = [character1]

tunnel.west = w_tunnel
w_tunnel.east = tunnel
a_room.east = stairs
b_room.west = living_room
c_room.east = living_room
stairs.west = player_room
stairs.down = living_room
living_room.up = stairs
living_room.north = kitchen
living_room.east = b_room
living_room.west = c_room
tunnel.west = w_tunnel
w_tunnel.west = end_tunnel
w_tunnel.east = tunnel
end_tunnel.north = skele_cave
end_tunnel.east = w_tunnel


playing = True

directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

overworld_actions = ['inventory', 'attack', 'take', 'scan', 'drop', 'help']
inventory_actions = ['equip', 'key', 'use']
short_over_actions = ['i', 'a', 't', 'sc', 'dr', 'h']


print("Type 'help' or 'h' for the commands.")

while playing is True:
    print("You awaken in a tunnel, with no memories other than you were struck down.")

    print()
    print(player.current_location.name)
    print(player.current_location.desc)
    print()

    for item in player.current_location.items:
        print("There is a %s in here" % item.name)
        if item is None:
            print("There are no items here.")

    command = input(">_")

    for player.current_location.enemies in player.current_location:
        player.current_location.enemies.attack(player)

    if player.health == 0:
        playing = False
        print("You died. "
              "To retry, press the play button again." 
              "Your progress has not been saved.")

    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    elif command.lower in short_over_actions:
        act = short_over_actions.index(command.lower())
        command = overworld_actions[act]

    elif command.lower() in ['q', 'quit', 'exit']:
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

    elif command.lower() in overworld_actions[0]:  # inventory
        print(player.inventory)
        if command.lower() == inventory_actions[2]:
            command = input(">_ What item do you want to use?")
            if command.lower() == Food:
                pass

    elif command.lower() in overworld_actions[1]:  # attack
        for enemy in player.current_location.enemies:
            print(enemy)
            p_target = input(">_ Which enemy do you want to attack?")
            if p_target == enemy.name:
                player.attack(enemy)
            command = input(">_ What do you want to want to do next?")

    elif command.lower() in overworld_actions[2]:  # take command
        phrase = input(">_ What do you want to take?")
        for item in player.current_location.items:
            if phrase == item.name:
                print("You take the %s" % item.name)
                player.inventory.append(item.name)
                player.current_location.items.remove(item)
            else:
                print("That item isn't in this room/ doesn't exist.")

    elif command.lower() in overworld_actions[3]:  # scan
        for item in player.current_location.items:
            print("There is a %s in here" % item.name)
            if item in player.current_location.items is None:
                print("There are no items here.")
        for i in range(len(player.current_location.characters)):
            print("There are %d characters in here." % len(player.current_location.characters))
            if i is None:
                print("There are no characters in here.")
        for i in range(len(player.current_location.enemies)):
            print("There are %d enemies in here." % len(player.current_location.enemies))
            if i is None:
                print("There are no enemies in here.")

    elif command.lower() in overworld_actions[4]:  # drop
        phrase = input(">_ What do you want to drop?")
        for item in player.current_location.items:
            if phrase == item.name:
                print("You drop the %s" % item.name)
                player.inventory.remove(item.name)
                player.current_location.items.append(item)
            else:
                print("You don't have that item.")

    elif command.lower() in overworld_actions[5]:  # help
        print("Move by typing the cardinal directions. Check rooms by typing 'scan' or 'sc'"
              "Pick up things by typing 'take' or 'ak'. 'Check your inventory by typing 'inventory' or 'i'"
              "Attack by typing 'a'.")
    else:
        print("Command Not Found")
