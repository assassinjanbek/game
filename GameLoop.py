from Map import Map
import Resolve

map = Map()

def loop(player):
    start = True
    while start:
        floor_name = map.display_choices(map.create_choices())
        if map.floor == 1:
            map.history[0] = floor_name
        else:
            map.history.append(floor_name)
        Resolve.resolve(floor_name, player)
        map.next_floor()
        if map.floor == 11:
            start = False
            Resolve.resolve("Boss", player)
    
