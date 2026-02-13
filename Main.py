import Character
import Menu
import Enemy_selection
import Combat
from Player import Player

def game():
    player = Player() 
    Menu.menu(player)
    Character.set_character(player)
    print(player)
    enemy = Enemy_selection.select_enemy()
    combat = Combat.Combat(enemy, player)
    combat.start_combat()
    print(player)

game()