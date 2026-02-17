from ColoredText import printcolor
from Enemy import Enemy
from Player import Player
from Roman import Roman
from inputcmd import inputcmd

class Combat:

    def players_dice(enemy, player):
        while True:
            print(
                f"You have {player.coin}\033[93m coin\033[0m\n"
                f"{player.dice_info()}\n"
                f"Choose a \033[32mdice\033[0m from your inventory\n"
            )
            action = inputcmd()
            if action == "coin":
                value = player.toss_a_coin()
                if value == 0:
                    continue
                else:
                    return value
            elif not action.isdigit():
                print("Please enter a number.")
                continue

            if 0 <= int(action) - 1 < len(player.inventory):
                die = player.inventory[int(action) - 1]
                return die
            else:
                print("Please enter a valid number. (For example, 1 for your first die)")
        


    def start_combat(enemy: Enemy, player: Player):
        round = 0

        print(
            f"Your enemy has {enemy.hp} hp."
            f"Your enemy will use \033[31m{enemy.die.quantity}, {enemy.die.side}\033[0m sided dice.\n"
        )
        input()

        while enemy.hp > 0 and player.hp > 0:
            print(f"\n - Round {Roman[round]} - \n")
            die = Combat.players_dice(enemy, player)
            if die == 1 or die == 2:
                print("You tossed a \033[93mcoin\033[0m! 🪙")
                players_value = die
            else:
                players_value = die.rolling() 
                if die.quantity == 0:
                    player.inventory.remove(die)

            if enemy.die.quantity < 1:
                enemy_value = 0
            else:
                enemy_value = enemy.die.rolling()

            if players_value > enemy_value:
                damage = players_value - enemy_value
                enemy.take_damage(damage)
            elif enemy_value > players_value:
                damage = enemy_value - players_value
                player.take_damage(damage)
            else:
                print("Tie!")

            print(
                f"\033[32mYou rolled {players_value}\033[0m\n"
                f"\033[31mEnemy rolled {enemy_value}\033[0m\n"
            )
            round += 1

            if enemy.hp > 0 and player.hp > 0:
                print(f"You have {player.hp} hp, enemy have {enemy.hp} hp\n")

        if enemy.hp <= 0:
            print(
                "- - - - - - - - - - - - - - - - - - - - - - - -\n"
                "Enemy hp is 0\n\033[32mYou beat the enemy! (〜￣▽￣)〜\033[0m\n"
                f"You gained \033[93m{enemy.prize}\033[0m \033[93mcoins\033[0m\n"
                "- - - - - - - - - - - - - - - - - - - - - - - -\n"
            )
            player.gain_coin(enemy.prize)
            player.score += int(enemy.prize / 2)
            input()