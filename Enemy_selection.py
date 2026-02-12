import random
from Enemy import Enemy
from Dice import Dice

def select_enemy():
    enemy_no = random.randint(1,5)
    if enemy_no == 1:
        die = Dice(4, 4)
        hp = 8
        prize = 3
    elif enemy_no == 2:
        die = Dice(6, 4)
        hp = 10
        prize = 5
    elif enemy_no == 3:
        die = Dice(20, 2)
        hp = 1
        prize = 8
    elif enemy_no == 4:
        die = Dice(12, 3)
        hp = 5
        prize = 8
    else:
        die = Dice(8, 8)
        hp = 8
        prize = 8
    enemy = Enemy(hp, die, prize)
    return enemy

