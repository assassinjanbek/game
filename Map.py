import random

class Map:

    def __init__(self):
        self.floor = 1
        self.history = ["Tavern"]
        self.a, self.b, self.c, self.d, self.e = 50, 20, 25, 15, 15
        self.pool = {"Merciful Enemy":self.a, "Cruel Enemy":self.b, "Event":self.c, "Market":self.d, "Tavern":self.e}

    def create_choices(self):
        self.a, self.b, self.c, self.d, self.e = 50, 20, 0, 15, 15
        filtered_pool = {}
        rmms = []
        wghts = []
        rooms = []
        for room, weight in self.pool.items():
            if  room == "Cruel Enemy" and self.floor < 5:
                continue
            if  room == "Tavern" and self.floor < 3:
                continue
            if  room == "Market" and self.floor < 3:
                continue
            if room == "Market" and self.history[-1] == "Market":
                continue
            if room == "Tavern" and self.history[-1] == "Tavern":
                continue
            if self.floor == 10:
                self.a, self.b, self.c, self.d, self.e = 10, 0, 0, 45, 30
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
            f"[1]> {rooms[0]}\n"
            f"[2]> {rooms[1]}\n")
            while True:
                ans = input("(1/2): ")
                if ans == "1" or ans == "2":
                    return rooms[int(ans)-1]
                else:
                    print("Write 1 or 2")

        if len(rooms) == 3:
            print("Choose your room:\n\n"
            f"[1]> {rooms[0]}\n"
            f"[2]> {rooms[1]}\n"
            f"[3]> {rooms[2]}\n")
            while True:
                ans = input("(1/2/3): ")
                if ans == "1" or ans == "2" or ans == "3":
                    return rooms[int(ans)-1]
                else:
                    print("Write 1 or 2 or 3")

    def next_floor(self):
        self.floor += 1