from Dice import Dice
from Player import Player

def character(player):

    player_hp = None
    player_coin = None
    player_i = None
    player_max = None
    name = None

    if player == "Gambler Wizard":
        player_i = [Dice(6, 15)]
        player_hp = 40
        player_max = 40
        player_coin = 10
        name = "Gambler Wizard"

    elif player == "Dice Wizard":
        player_i = [Dice(6, 5), Dice(8, 5), Dice(10, 5)]
        player_hp = 35
        player_max = 35
        player_coin = 0
        name = "Dice Wizard"

    player = Player(player_hp, player_coin, player_i, player_max, name)
    
    return player

