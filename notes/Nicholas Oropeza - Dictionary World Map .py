world_map = {
    'CLOSET': {
        'NAME': "The Closet",
        'DESCRIPTION': "You're in the closet. There's a lock on the door. " 
                       "Check your pockets by pressing 'e'",
        'PATHS': {
              'WEST': "SHAGGY'S_ROOM",
              'UP': "MARINA"
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
