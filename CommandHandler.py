import os
import sys
import Character
from ColoredText import printcolor
from Combat import Combat
from Enemy_selection import select_enemy
from Game import GameState
from Player import Player
import Events


# Önce state'e bakıyor, sonra ona göre komut işliyor. 
# Mesela start menüsünde yes/no/info komutları geçerli, diğerleri değil.

def handle_command(cmd: str, game):

    parts = cmd.split() # (python kodu çok yararlı)
    if len(parts) != 0:
        command = parts[0]
        args = parts[1:]
        if command == "exit":
            print("wizards will haunt you...")
            game.running = False
            return
        if command == "help":
            print("You can: help, exit, inventory, status, score")
            return
        elif command == "inventory":
            if not game.player.inventory:
                print("Your inventory is empty.")
            else:
                print("Your inventory:") # chatgpt yaptı
                for idx, item in enumerate(game.player.inventory, 1):
                    print(f"{idx}) {item.quantity}x {item.side}-sided die")
            return
        elif command == "status":
            print(f"Your health: {game.player.hp}")
            print(f"Your coins: {game.player.coin}")
            return
        elif command == "use":
            Events.use_item(args, game.player) # Events daha yapmadım, göstermelik
            return
        
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
    
    # CHARACTER SELECTION menüsü
    elif game.state == GameState.MENU:
        if cmd == "1":
            printcolor("\nYou chose Dice Wizard.\n\n\n", "blue")
            game.player = Player("Dice Wizard")
            Character.set_character(game.player)
            game.state = GameState.EXPLORING
        elif cmd == "2":
            printcolor("\nYou chose Gambler Wizard.\n\n\n", "magenta")
            game.player = Player("Gambler Wizard")
            Character.set_character(game.player)
            game.state = GameState.EXPLORING
        else:
            print("Type 1 for Dice Wizard or 2 for Gambler Wizard.")
    
    # EXPLORING yazdığım 
    elif game.state == GameState.EXPLORING:
        if cmd == "":
            game.current_enemy = select_enemy()
            game.state = GameState.COMBAT
        else:
            print("now is not the time for that, just press enter to explore the world")
    
    # COMBAT sekansı
    elif game.state == GameState.COMBAT:
        Combat.start_combat(game.current_enemy, game.player)
        if game.player.hp <= 0:
            game.state = GameState.GAME_OVER
        else:
            game.current_enemy = None
            game.state = GameState.EXPLORING
    
    elif game.state == GameState.GAME_OVER:
        game.running = False