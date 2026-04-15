import random

class Dice:
    def __init__(self, side, quantity):
        self.side = int(side)
        self.quantity = int(quantity)

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side):
        self._side = int(side)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = int(quantity)

    def rolling(self):
        value = random.randint(1, self.side)
        self.quantity -= 1
        return value
    
    def __str__(self):
        return f"\033[95m{self.quantity}, {self.side}\033[0m sided dice \n"

def main():
    six_sided_dice = Dice(6, 5)
    while six_sided_dice.quantity > 0:
        ans = input(f"You have {six_sided_dice.quantity} dice \nYou wanna roll them? (yes/no): ")
        if ans == "yes":
            print(six_sided_dice.rolling())
        if ans == "no":
            print("ok bye!")
            return 

        
