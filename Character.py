from Dice import Dice
from Player import Player

def set_character(player: Player):

    if player.character == "Gambler Wizard":
        player.inventory = [Dice(6, 15)]
        player.hp = 40
        player.coin = 10
    elif player.character == "Dice Wizard":
        player.inventory = [Dice(6, 6), Dice(10, 6)]
        player.hp = 35
        player.coin = 0