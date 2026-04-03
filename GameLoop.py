from Map import Map
import Resolve

map = Map()

def loop(player):
    start = True
    while start:
        floor_name = map.display_choices(map.create_choices())
        if map.floor == 0:
            map.history[0] = floor_name
        map.history.append(floor_name)
        Resolve.resolve(floor_name, player)
        map.next_floor()
        if map.floor == 10:
            start = False