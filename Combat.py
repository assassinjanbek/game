import sys
from Enemy import Enemy
from Player import Player
from Dice import Dice

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
        print(f"\nYou've encountered {self.enemy.color}{self.enemy.name}\033[0m!")
        round_ = 1
        print(f"\nYour enemy has \033[91m{self.enemy.hp} hp\033[0m.")
        print(f"Your enemy will use \033[95m{self.enemy.die.quantity}, {self.enemy.die.side}\033[0m sided dice.\n")

        while self.enemy.hp > 0 and self.player.hp > 0:
            print(f"- Round {round_} -")
            print(f"\n{self.enemy.general_info()}")
            die = self.players_dice()
            if die == 1 or die == 2:
                print("You tossed a\033[93m coin\033[0m! 🪙")
                players_value = die
            else:
                players_value = die.rolling()
                if die.quantity == 0:
                    self.player.inventory.remove(die)

            if self.enemy.die.quantity < 1:
                enemy_value = 0
            else:
                enemy_value = self.enemy.die.rolling()

            print(
            f"\nYou rolled \033[95m{players_value}\033[0m\n"
            f"Enemy rolled \033[95m{enemy_value}\033[0m\n"
            )

            if players_value > enemy_value:
                damage = players_value - enemy_value
                print(f"You dealt \033[92m{damage}\033[0m damage.\n")
                self.enemy.take_damage(damage)
            elif enemy_value > players_value:
                damage = enemy_value - players_value
                print(f"You took \033[91m{damage}\033[0m damage.\n")
                self.player.take_damage(damage)
            else:
                print("\033[94mTie!\033[0m\n")


            round_ += 1

        if self.enemy.hp <= 0:
            print("Enemy \033[91mhp is \033[91m0\033[0m\n\033[92mYou beat the enemy! (〜￣▽￣)〜\033[0m\n"
            f"You gained {self.enemy.prize} \033[93mcoins\033[0m\n"    
            )
            self.player.gain_coin(self.enemy.prize)
            if self.enemy.die.quantity > 0:
                die_found = None
                for die in self.player.inventory:
                    if die.side == self.enemy.die.side:
                        die_found = die
                        break
                if die_found:
                    die_found.quantity += self.enemy.die.quantity
                else:
                    self.player.inventory.append(Dice(self.enemy.die.side, self.enemy.die.quantity))
                print(f"You took \033[95m{self.enemy.die.quantity}, {self.enemy.die.side}\033[0m sided dice from the enemy.\n")
            self.player.general_info()
        elif not self.player.inventory and self.player.coin == 0:
            self.player.hp = 0
            print("You \033[91mdied\033[0m from misery. Poor wizard, nobody will remember you.")
            sys.exit()
        else:
            print("You are \033[91mdead.\033[0m Sorry.（＞人＜；）")
            sys.exit()
            
    def players_dice(self):
        while True:
            no = input(f"{self.player.general_info()}"
                       f"Choose a die from your inventory: ").strip()
            if no == "c":
                value = self.player.toss_a_coin()
                if value == 0:
                    continue
                else:
                    return value
            elif not no.isdigit():
                print("\nPlease enter a number.")
                continue

            if 0 <= int(no) - 1 < len(self.player.inventory):
                die = self.player.inventory[int(no) - 1]
                return die
            else:
                print("\nPlease enter a valid number. (For example, 1 for your first die)")
        
