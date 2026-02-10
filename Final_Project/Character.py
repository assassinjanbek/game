from Dice import Dice
from Player import Player

def character(player):

    gambler_hp = None
    gambler_coin = None
    gambler_i = None

    if player == "Gambler Wizard":
        gambler_i = [Dice(6, 15)]
        gambler_hp = 40
        gambler_coin = 10
    elif player == "Dice Wizard":
        gambler_i = [Dice(6, 6), Dice(10, 6)]
        gambler_hp = 35
        gambler_coin = 0

    player = Player(gambler_hp, gambler_coin, gambler_i)
    
    return player

