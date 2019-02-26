class Room(object):
    def __int__(self, name, desc, north=None, south=None, east=None, west=None, up=None, down=None):
        self.name = name
        self.desc = desc
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down


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

    closet = Room("Anton's Closet", "You're in the closet.")
    anton_room = Room("Anton's Room", "There's something under his bed.")
    tunnel = Room("Dark Tunnel", "Dark, Dank Tunnel")
    w_tunnel = Room("West Tunnel", "Dark, Dank Tunnel, but to the West")
    skele_cave = Room("The Skeleton Cave", "There are at least 100 skeletons in here.")
    end_tunnel = Room("The end of the tunnel.")
    jaiden_room = Room("Jaiden's Room", "placeholder")
    stairs = Room("The staircase",
                  "A staircase in between two rooms in the middle of the hallway.")
    a_room = Room("A room", "?")
    living_room = Room("The Living Room", "placeholder")
    player_room = Room("Your Room", "The room is messy.")
    kitchen = Room("The Kitchen", "placeholder desc")
    b_room = Room("B room", "placeholder desc")
    c_room = Room("C room", "placeholder desc")

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
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
