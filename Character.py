from Dice import Dice
from Player import Player

def set_character(player: Player):

    if player.character == "Gambler Wizard":
        player._inventory = [Dice(6, 15)]
        player._hp = 40
        player._coin = 10
    elif player.character == "Dice Wizard":
        player._inventory = [Dice(6, 6), Dice(10, 6)]
        player._hp = 35
        player._coin = 0