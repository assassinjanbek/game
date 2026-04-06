import sys
from Enemy import Enemy
from Player import Player

class Combat:
    def __init__(self, enemy: Enemy, player: Player):
        self.enemy = enemy
        self.player = player

    @property
    def enemy(self):
        return self._enemy

    @enemy.setter
    def enemy(self, enemy):
        self._enemy = enemy

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        self._player = player

    def start_combat(self):

        print(f"Your enemy has {self.enemy.hp} hp.")
        print(f"Your enemy will use {self.enemy.die.quantity}, {self.enemy.die.side} sided dice.\n")

        while self.enemy.hp > 0 and self.player.hp > 0:
            die = self.players_dice()
            if die == 1 or die == 2:
                print("You tossed a coin! 🪙")
                players_value = die
            else:
                players_value = die.rolling() 
                if die.quantity == 0:
                    self.player.inventory.remove(die)

            if self.enemy.die.quantity < 1:
                enemy_value = 0
            else:
                enemy_value = self.enemy.die.rolling()

            if players_value > enemy_value:
                damage = players_value - enemy_value
                self.enemy.take_damage(damage)
            elif enemy_value > players_value:
                damage = enemy_value - players_value
                self.player.take_damage(damage)
            else:
                print("Tie!")

            print(
                f"You rolled {players_value}\n"
                f"Enemy rolled {enemy_value}\n"
            )

            if self.enemy.hp > 0 and self.player.hp > 0:
                print(f"You have {self.player.hp} hp, enemy have {self.enemy.hp} hp\n")

        if self.enemy.hp <= 0:
            print("Enemy hp is 0\nYou beat the enemy! (〜￣▽￣)〜\n"
            f"You gained {self.enemy.prize} coins"    
            )
            self.player.gain_coin(self.enemy.prize)
        else:
            print("You are dead. Sorry.（＞人＜；）")
            sys.exit()
            
    def players_dice(self):
        while True:
            no = input(f"You have {self.player.coin} coin\n{self.player.dice_info()}\nChoose a dice from your inventory: ").strip()
            if no == "coin":
                value = self.player.toss_a_coin()
                if value == 0:
                    continue
                else:
                    return value
            elif not no.isdigit():
                print("Please enter a number.")
                continue

            if 0 <= int(no) - 1 < len(self.player.inventory):
                die = self.player.inventory[int(no) - 1]
                return die
            else:
                print("Please enter a valid number. (For example, 1 for your first die)")
        
