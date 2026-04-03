import random

class Map:

    def __init__(self):
        self.floor = 0
        self.history = ["Tavern"]
        self.pool = {"Merciful Enemy":40, "Cruel Enemy":10, "Event":20, "Market":10, "Tavern":10}
        self.special_floor = 10

    def create_choices(self):
        filtered_pool = {}
        rmms = []
        wghts = []
        rooms = []
        for room, weight in self.pool.items():
            if  room == "Cruel Enemy" and self.floor < 4:
                continue
            if room == "Market" and self.history[-1] == "Market":
                continue
            if room == "Tavern" and self.history[-1] == "Tavern":
                continue
            filtered_pool[room] = weight
        for room in filtered_pool:
            rmms.append(room)
        for weight in filtered_pool.values():
            wghts.append(weight)
        n_choice = random.randint(2,3)
        rooms = random.choices(rmms, weights=wghts, k=n_choice)
        return rooms

    def display_choices(self, rooms):
        if len(rooms) == 2:
            print("Choose your room:\n\n"
            f"> {rooms[0]}\n"
            f"> {rooms[1]}\n")
            while True:
                ans = input("1 or 2: ")
                if ans == "1" or ans == "2":
                    return rooms[int(ans)-1]
                else:
                    print("Write 1 or 2")

        if len(rooms) == 3:
            print("Choose your room:\n\n"
            f"> {rooms[0]}\n"
            f"> {rooms[1]}\n"
            f"> {rooms[2]}\n")
            while True:
                ans = input("1 or 2 or 3: ")
                if ans == "1" or ans == "2" or ans == "3":
                    return rooms[int(ans)-1]
                else:
                    print("Write 1 or 2 or 3")

    def next_floor(self):
        self.floor += 1