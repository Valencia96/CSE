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
    living_room = ("The Living Room", "placeholder")


    closet.west = anton_room
    anton_room.east = closet
    anton_room.down = tunnel
    anton_room.north = jaiden_room
    jaiden_room.west = stairs
    jaiden_room.south = anton_room
    a_room.east = stairs
    stairs.east = jaiden_room
    stairs.west = kitchen
    tunnel.west = w_tunnel
    tunnel.up = anton_room
    w_tunnel.west = end_tunnel
    w_tunnel.east = tunnel
    end_tunnel.north = skele_cave
    end_tunnel.east = w_tunnel


"""
# Option 1 - Define as we go
    R19A = Room("Mr. Wiebe's Room")
    parking_lot = Room("Parking Lot", None, R19A)

    R19A.north = parking_lot
# Option 2 - Set all at once, modify controller
    R19A = Room("Mr. Wiebe's Room", 'parking_lot')
    parking_lot = Room("Parking Lot", None, R19A)
"""
