import Character
from Game import Game
import Menu
import Enemy_selection
from Combat import Combat
from Player import Player
from ColoredText import printcolor, inputcolor

def game():
    game = Game()
    game.run()

game()