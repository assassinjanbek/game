import os
import sys
from ColoredText import printcolor
from Combat import Combat
from Enemy_selection import select_enemy
from Game import GameState
from Player import Player
import Events


# Önce state'e bakıyor, sonra ona göre komut işliyor. 
# Mesela start menüsünde sadece yes/no/info komutları geçerli, diğerleri değil.

def handle_command(cmd: str, game):
    
    # START Menüsü
    if game.state == GameState.START:
        if cmd == "yes":
            game.state = GameState.MENU
        elif cmd == "no":
            print("ok bye!")
            sys.exit()
        elif cmd == "info":
            print("Project J:\n\n"
            "Project J is a simple, luck and strategy based game.\n"
            "All you have to do is choosing a wizard, and going trough an extraordinary adventure.\n\n"
            "How to play:\n\n"
            "During your adventure, you'll face up with many different things,\n"
            "One of them is strange enemmies. When you encounter with an enemy, you have two different option.\n"
            "You can choose an item (probably a dice) from your inventory or your can toss a coin.\n"
            "If you desire to use your first item, you should type 1, and similarly 2 for your second item.\n"
            "If you desire to toss a coin, which counts as a two sided dice, you should simply type 'coin' (you will lose a coin).\n"
            "I think you should explore the rest of the game by yourself. Have fun!\n")
        else:
            print("Please type 'yes' to start or 'info' for more information, or 'no' to remain unsatisfied.")
        return

    parts = cmd.split() # python kodu çok yararlı
    # if not parts:
    #     return
    
    # CHARACTER SELECTION menüsü
    if game.state == GameState.MENU:
        if parts[0] == "1":
            printcolor("You chose Dice Wizard.\n", "blue")
            game.player = Player("Dice Wizard")
            game.state = GameState.EXPLORING
        elif parts[0] == "2":
            printcolor("You chose Gambler Wizard.\n", "magenta")
            game.player = Player("Gambler Wizard")
            game.state = GameState.EXPLORING
        else:
            print("Type 1 for Dice Wizard or 2 for Gambler Wizard.")
        return
    
    # EXPLORING yazdığım 
    if game.state == GameState.EXPLORING:
        game.current_enemy = select_enemy()
        game.state = GameState.COMBAT
        return
    
    # COMBAT sekansı
    if game.state == GameState.COMBAT:
        Combat.start_combat(game.current_enemy, game.player)
        if game.player.hp <= 0:
            game.state = GameState.GAME_OVER
            return
        else:
            printcolor(f"You defeated the {game.current_enemy.name}!", "green")
        return
    
    if not parts:
            return
    command = parts[0]
    args = parts[1:]
    if command == "exit":
        print("wizards will haunt you...")
        game.running = False
    if command == "help":
        print("You can: help, exit, inventory, status, score")
    elif command == "use":
        Events.use_item(args, game.player) 
    # elif command == "inventory":
    #     print("Your inventory: ")
    #     game.player.print_inventory()
    # elif command == "status":
    #     print("Your status: ")
    #     game.player.print_status()
    # elif command == "score":
    #     print("Your score is: ")
    #     game.player.print_score()
    else:
        print("Unknown command. Type 'help' for a list of commands.")
