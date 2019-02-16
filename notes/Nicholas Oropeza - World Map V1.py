world_map = {
    'CLOSET': {
        'NAME': "The Closet",
        'DESCRIPTION': "You're in the closet. "
                       "Don't worry you're not locked in.",
        'PATHS': {
            'WEST': "SHAGGY_ROOM",
        }
    },
    'TUNNEL': {
        'NAME': "Dark Tunnel",
        'DESCRIPTION': "Dark, Dank Tunnel.",
        'PATHS': {
            'WEST': "W_TUNNEL",
            'UP': "SHAGGY_ROOM"
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
            'NORTH': "SKELE_CAVE"
        }
    },
    'SKELE_CAVE': {
        'NAME': "The Skeleton Cave.",
        'DESCRIPTION': "Yup, you're definitely in the Skeleton Cave. " 
                       "There's at least 100 skeletons in here.",
        'PATHS': {
            'SOUTH': "END_W_TUNNEL",
        }
    },
    'SHAGGY_ROOM': {
        'NAME': "HIS Room",
        'DESCRIPTION': "This is Shaggy's room, why are you in here? "
                       "There's something under his bed.",
        'PATHS': {
            'EAST': "CLOSET",
            'DOWN': "TUNNEL",
            'NORTH': "MARINA_ROOM"
        }
    },
    'MARINA_ROOM': {
        'NAME': "Marina's Room",
        'DESCRIPTION': "You're in Marina's Room. ",
        'PATHS': {
            'WEST': "STAIRS",
            'SOUTH': "SHAGGY_ROOM",
            'EAST': "MARINA_BATH"

        }
    },
    'MARINA_BATH': {
        'NAME': "Marina's restroom",
        'DESCRIPTION': "You're in Marina's restroom. " 
                       "Why are you in Marina's restroom?"
                       "You have your own restroom.",
        'PATHS': {
            'WEST': "MARINA_ROOM"
        }
    },

    'STAIRS': {
        'NAME': "The Staircase",
        'DESCRIPTION': "You're at the staircase. "
                       "There's a room across the hall.",
        'PATHS': {
            'WEST': "PLAYER_ROOM",
            "DOWN": "LIVING_ROOM"
        }
    },
    'LIVING_ROOM': {
        'NAME': "The Living Room.",
        'DESCRIPTION': "You're in the living room. ",
        'PATHS': {
            'EAST': "GUEST",
            'WEST': "KITCHEN",
            'UP': "STAIRS"
        }
    },
    'GUEST': {
        'NAME': "The Guest Room.",
        'DESCRIPTION': "You're in the guest room. The bed's covers are dirty.",
        'PATHS': {
            'WEST': "LIVING_ROOM"
        }
    },
    'KITCHEN': {
        'NAME': "The Kitchen.",
        'DESCRIPTION': "You're in the kitchen. " 
                       "The sink's full and the stove is off.",
        'PATHS': {
            'EAST': "LIVING_ROOM"
        }
    },
    'PLAYER_ROOM': {
        'NAME': "Your Room.",
        'DESCRIPTION': "You're in your room. " 
                       "The bed is all messed up and the desk has a lot of stuff on it.",
        'PATHS': {
            'WEST': "BATHROOM",
            'EAST': "STAIRS"
        }
    },
    'BATHROOM': {
        'NAME': "The Restroom.",
        'DESCRIPTION': "You're in your own personal restroom. ",
        'PATHS': {
            'WEST': "PLAYER_ROOM",
        },
    }
}

# Controller
playing = True
current_node = world_map['CLOSET']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

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
    else:
        print("Command Not Found")
