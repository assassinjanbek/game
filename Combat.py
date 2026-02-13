# başarılı baya combatı yazarken classları çözmüşsün
from Enemy import Enemy
from Player import Player

class Combat:

    def players_dice(enemy, player):
        while True:
            no = input(f"You have {player.coin} coin\n{player.dice_info()}\nChoose a dice from your inventory: ").strip()
            if no == "coin":
                value = player.toss_a_coin()
                if value == 0:
                    continue
                else:
                    return value
            elif not no.isdigit():
                print("Please enter a number.")
                continue

            if 0 <= int(no) - 1 < len(player.inventory):
                die = player.inventory[int(no) - 1]
                return die
            else:
                print("Please enter a valid number. (For example, 1 for your first die)")
        


    def start_combat(enemy: Enemy, player: Player):

        print(f"Your enemy has {enemy.hp} hp.")
        print(f"Your enemy will use {enemy.die.quantity}, {enemy.die.side} sided dice.\n")

        while enemy.hp > 0 and player.hp > 0:
            die = Combat.players_dice(enemy, player)
            if die == 1 or die == 2:
                print("You tossed a coin! 🪙")
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
                f"You rolled {players_value}\n"
                f"Enemy rolled {enemy_value}\n"
            )

            if enemy.hp > 0 and player.hp > 0:
                print(f"You have {player.hp} hp, enemy have {enemy.hp} hp\n")

        if enemy.hp <= 0:
            print(
                "Enemy hp is 0\nYou beat the enemy! (〜￣▽￣)〜\n"
                f"You gained {enemy.prize} coins"    
            )
            player.gain_coin(enemy.prize)
        else:
            print("You are dead. Sorry.（＞人＜；）")