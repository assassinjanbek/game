import random
from Enemy import Enemy
from Dice import Dice

def select_merciful_enemy():
    enemy_no = random.randint(1,5)
    if enemy_no == 1:
        die = Dice(4, 4)
        hp = 4
        prize = 3
        name = "Watermelon Chameleon"
        color = "\033[91m"
    elif enemy_no == 2:
        die = Dice(6, 4)
        hp = 10
        prize = 6
        name = "Honorable Knight"
        color = "\033[90m"
    elif enemy_no == 3:
        die = Dice(8, 2)
        hp = 14
        prize = 8
        name = "Depressive Ogre"
        color = "\033[91m"
    elif enemy_no == 4:
        die = Dice(12, 3)
        hp = 5
        prize = 8
        name = "The Rogue"
        color = "\033[93m"
    else:
        die = Dice(6, 6)
        hp = 6
        prize = 8
        name = "Extremely Drunk Elf"
        color = "\033[93m"
    enemy = Enemy(hp, die, prize, name, color)
    return enemy

def select_cruel_enemy():
    enemy_no = random.randint(1,3)
    if enemy_no == 1:
        die = Dice(20, 2)
        hp = 2
        prize = 15
        name = "Crazy Old Man"
        color = "\033[90m"
    elif enemy_no == 2:
        die = Dice(12, 4)
        hp = 6
        prize = 15
        name = "Bloodthirsty Lizard"
        color = "\033[91m"
    else:
        die = Dice(8, 8)
        hp = 8
        prize = 15
        name = "Strong Minded Fighter"
        color = "\033[94m"
    enemy = Enemy(hp, die, prize, name, color)
    return enemy

def select_boss():
    enemy_no = random.randint(1,2)
    if enemy_no == 1:
        die = Dice(10, 20)
        hp = 15
        prize = 100
        name = "Dungeon Master"
        color = "\033[95m"
    else:
        die = Dice(12, 12)
        hp = 20
        prize = 100
        name = "Silk Queen"
        color = "\033[95m"
    enemy = Enemy(hp, die, prize, name, color)
    return enemy
