from Map import Map
import Resolve

map_ = Map()

def loop(player):
    start = True
    while start:
        floor_name = map_.display_choices(map_.create_choices())
        if map_.floor == 1:
            map_.history[0] = floor_name
        else:
            map_.history.append(floor_name)
        Resolve.resolve(floor_name, player)
        map_.next_floor()
        if map_.floor == 16:
            start = False
    
