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

    closet = Room("Shaggy's Closet", "You're in the closet.")
    tunnel = Room("Dark Tunnel", "Dark, Dank Tunnel")
    w_tunnel = Room("West Tunnel", "Dark, Dank Tunnel, but to the West")
    end_tunnel = Room("The end of the tunnel.")
    shaggy_room = Room("")

    closet.west = shaggy_room
    tunnel.west = w_tunnel
    tunnel.up = shaggy_room
    w_tunnel.west = end_tunnel
    w_tunnel.east = tunnel


"""
# Option 1 - Define as we go
    R19A = Room("Mr. Wiebe's Room")
    parking_lot = Room("Parking Lot", None, R19A)

    R19A.north = parking_lot
# Option 2 - Set all at once, modify controller
    R19A = Room("Mr. Wiebe's Room", 'parking_lot')
    parking_lot = Room("Parking Lot", None, R19A)
"""
