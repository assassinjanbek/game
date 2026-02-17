import random
from Enemy import Enemy
from Dice import Dice

def select_enemy() -> Enemy:
    enemy_no = random.randint(1,5)
    if enemy_no == 1:
        name = "\033[93mGoblin\033[0m"
        die = Dice(4, 4)
        hp = 8
        prize = 3
    elif enemy_no == 2:
        name = "\033[92mOrc\033[0m"
        die = Dice(6, 4)
        hp = 10
        prize = 5
    elif enemy_no == 3:
        name = "\033[90mTroll\033[0m"
        die = Dice(20, 2)
        hp = 1
        prize = 8
    elif enemy_no == 4:
        name = "\033[97mBandit\033[0m"
        die = Dice(12, 3)
        hp = 5
        prize = 8
    else:
        name = "\033[91mDragon\033[0m"
        die = Dice(8, 8)
        hp = 8
        prize = 8

    return Enemy(name, hp, die, prize)