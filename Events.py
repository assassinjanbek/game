import random
from Player import Player

class Event:
    def __init__(self, player: Player):
        self.player = player
        self.event_no = random.randint(1,5)

    def start_event(self):
        print("Oh, that is a rock!")