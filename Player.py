import random
from Dice import Dice

class Player:
    
    def __init__(self, hp, coin, inventory, max_hp, name):
        self.max_hp = int(max_hp)
        self.hp = int(hp)
        self.coin = int(coin)
        self.inventory = list(inventory)
        self.name = name
        

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        value = int(hp)
        if value > self.max_hp:
            value = self.max_hp
        self._hp = value

    @property
    def coin(self):
        return self._coin
    
    @coin.setter
    def coin(self, coin):
        value = int(coin)
        if value < 0:
            value = 0
        self._coin = value

    @property
    def inventory(self):
        return self._inventory
    
    @inventory.setter
    def inventory(self, inventory):
        self._inventory = list(inventory)

    def take_damage(self, damage):
        self.hp -= damage

    def heal(self, heal):
        self.hp += heal
        print("\nYou've recovered \033[91m5 hp\033[0m.")

    def spend_coin(self, price):
        if (self.coin - price) < 0:
            print("\nYou don't have enough coin")
            return 0
        else:
            self.coin -= price

    def gain_coin(self, price):
        self.coin += price

    def gain_dice(self, q, d):
        die_found = None
        for die in self.inventory:
            if die.side == d:
                die_found = die
                break
        if die_found:
            die_found.quantity += q
        else:
            self.inventory.append(Dice(d, q))
    
    def toss_a_coin(self):
        if self.coin == 0:
            print("\nYou don't have any coin")
            return 0
        else:
            value = random.randint(1,2)
            self.coin -= 1
            return value

    def dice_info(self):
        message = ""
        for dice in self.inventory:
            message += f"[{(self.inventory.index(dice)) + 1}] {str(dice)}"
        return message
    
    def general_info(self):
        message = (f"\nYour \033[91mhp\033[0m is \033[91m{self.hp}\033[0m/{self.max_hp} ❤️\nYou have \033[93m{self.coin} coin\033[0m 🪙\n"
        f"Your dices 🎲 :\n{self.dice_info()}\n")
        return message
