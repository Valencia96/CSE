world_map = {
    'CLOSET': {
        'NAME': "The Closet",
        'DESCRIPTION': "You're in the closet. There's a lock on the door. "
                       "Check your pockets.",
        'PATHS': {
            'WEST': "SHAGGY'S_ROOM",
            'UP': "MARINA",
            'DOWN': "TUNNEL"
        }
    },
    'TUNNEL': {
        'NAME': "Dark Tunnel",
        'DESCRIPTION': "Dark, Dank Tunnel.",
        'PATHS': {
            'WEST': "W_TUNNEL",
            'DOWN': "ENT_HELL"
        }
    },
    'W_TUNNEL': {
        'NAME': "West Tunnel",
        'DESCRIPTION': "Dark, Dank Tunnel but to the West. ",
        'PATHS': {
            'WEST': "END_W_TUNNEL",
            'EAST': "W_TUNNEL"
        }
    },
    'END_W_TUNNEL': {
        'NAME': "The end of the tunnel. ",
        'DESCRIPTION': "End of the tunnel, there's NOTHING WEST beyond this point.",
        'PATHS': {
            'WEST': "",
            'NORTH': "SKELE_CAVE"
        }
    },
    'SHAGGY\'S_ROOM': {
        'NAME': "HIS Room",
        'DESCRIPTION': "This is HIS room why are you in here? "
                       "There's something glistening under HIS bed.",
        'PATHS': {
            'EAST': "CLOSET"
        }
    },
    'MARINA': {
        'NAME': "Marina's Room",
        'DESCRIPTION': "You're in Marina's Room. ",
        'PATHS': {
            'WEST': "STAIRS",
            "DOWN": "SHAGGY'S ROOM"
        }
    },
    'STAIRS': {
        'NAME': "The Staircase",
        'DESCRIPTION': "You're at the staircase. "
                       "There's a room across the hall.",
        'PATHS': {
            'WEST': "YOUR_ROOM",
            "DOWN": "LIVING_ROOM"
        }
    },
    'LIVING_ROOM': {
        'NAME': "The Living Room.",
        'DESCRIPTION': "You're in the living room. ",
        'PATHS': {
            'EAST': "GUEST",
            'SOUTH': "LIVING_ROOM",
            'WEST': "KITCHEN",
            'UP': "STAIRS"
        }
    },

}

# Controller
playing = True
current_node = world_map['CLOSET']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
actions = ['INV', 'PICKUP']
inv = ['Closet Key']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    elif command.upper() in actions:
        try:
            pass
        except KeyError:
            pass
    else:
        print("Command Not Found")
