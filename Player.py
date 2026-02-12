import random

class Player:
    
    def __init__(self, hp, coin, inventory):
        self.hp = int(hp)
        self.coin = int(coin)
        self.inventory = list(inventory)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = int(hp)

    @property
    def coin(self):
        return self._coin
    
    @coin.setter
    def coin(self, coin):
        self._coin = int(coin)

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

    def spend_coin(self, price):
        self.coin -= price

    def gain_coin(self, price):
        self.coin += price
    
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
            message += f"{str(dice)}"
        return message

    def __str__(self):
        return f"Your hp ❤️ : {self.hp}\nYour coins 🪙 : {self.coin}\nYour dices 🎲: \n{self.dice_info()}"
