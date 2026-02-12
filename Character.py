from Dice import Dice
from Player import Player

def character(player):

    player_hp = None
    player_coin = None
    player_i = None

    if player == "Gambler Wizard":
        player_i = [Dice(6, 15)]
        player_hp = 40
        player_coin = 10
    elif player == "Dice Wizard":
        player_i = [Dice(6, 6), Dice(10, 6)]
        player_hp = 35
        player_coin = 0

    player = Player(player_hp, player_coin, player_i)
    
    return player

