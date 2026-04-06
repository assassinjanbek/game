import random

class Player:
    
    def __init__(self, hp, coin, inventory, max_hp):
        self.hp = int(hp)
        self.coin = int(coin)
        self.inventory = list(inventory)
        self.max_hp = int(max_hp)

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

    def spend_coin(self, price):
        if (self.coin - price) < 0:
            print("\nYou don't have enough coin")
            return 0
        else:
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
