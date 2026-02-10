import random
from Enemy import Enemy
from Dice import Dice

def select_enemy():
    enemy_no = random.randint(1,5)
    if enemy_no == 1:
        die = Dice(4, 4)
        enemy = Enemy(3, die)
    elif enemy_no == 2:
        die = Dice(6, 4)
        enemy = Enemy(5, die)
    elif enemy_no == 3:
        die = Dice(20, 2)
        enemy = Enemy(2, die)
    elif enemy_no == 4:
        die = Dice(12, 3)
        enemy = Enemy(6, die)
    else:
        die = Enemy(8, 8)
        enemy = Enemy(8, die)
    return enemy

