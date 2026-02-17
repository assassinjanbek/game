import Character
import Menu
import Enemy_selection
from Combat import Combat
from Player import Player
from ColoredText import printcolor, inputcolor

def game():
    player = Player() 
    Menu.menu(player)
    Character.set_character(player)

    # Game Loop
    while player.hp > 0:
        print(player)
        enemy = Enemy_selection.select_enemy()
        Combat.start_combat(enemy, player)

    printcolor("You are dead. Sorry.（＞人＜；）", "red")
    return

game()