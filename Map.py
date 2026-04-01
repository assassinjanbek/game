import random

class Map:

    def __init__(floor, choices, n_choice):
        self.floor = int(floor)
        self.choices = choices
        self.n_choice = n_choice
        self.history = []
        self.pool = ["Merciful Enemy", "Cruel Enemy", "Event", "Market", "Tavern"]
        self.special_floor = 10

    def pool_filter(self, pool):

    def create_choices(self, floor, n_choice, pool, history):
        filtered_pool = []
        for room in pool:
            if room == "Cruel Enemy" and self.floor < 4:
                continue
            elif room == "Market" and self.history[floor - 1] == "Market":
                continue
            elif room == "Tavern" and self.history[floor - 1] == "Tavern":
                continue
        n_choice = random.randint(2,3)
        filtered_pool.append(room)

        
    def display_choices(self, choices):

    def user_input():

    def next_floor(self, floor):
        floor += 1