import os
import random
import sys
import Character
from ColoredText import printcolor
from Combat import Combat
from Dice import Dice
from Enemy_selection import select_enemy
from Game import GameState
import Messages
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
            print("You can: help, exit, inventory, status, market, score")
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
        elif command == "score":
            print(f"Your score: {game.player.score}")
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
            luck = random.randint(1, 100)
            if luck <= 40:  # %40 ihtimalle düşmanla karşılaşılır
                game.current_enemy = select_enemy()
                game.state = GameState.COMBAT
            elif luck <= 70:  # %30 ihtimalle bir şey bulunur
                print("You found a coin!")
                game.player.coin += 1
            else:  # %30 ihtimalle hiçbir şey olmaz
                print(Messages.Explore[random.randint(0, len(Messages.Explore) - 1)])
        elif cmd == "market":
            print("Welcome to the market! Here you can buy dice with your coins.")
            print("Available dice:")
            print("1) 6-sided die (cost: 2 coin)")
            print("2) 10-sided die (cost: 3 coins)")
            print("Type the number of the die you want to buy, or 'leave' to leave the market.")
            while True:
                market_cmd = input().strip().lower()
                if market_cmd == "leave":
                    print("Leaving the market...")
                    break
                elif market_cmd == "1":
                    if game.player.coin >= 2:
                        game.player.coin -= 2
                        game.player.inventory.append(Dice(6, 1))
                        print("You bought a 6-sided die!")
                    else:
                        print("You don't have enough coins.")
                elif market_cmd == "2":
                    if game.player.coin >= 3:
                        game.player.coin -= 3
                        game.player.inventory.append(Dice(10, 1))
                        print("You bought a 10-sided die!")
                    else:
                        print("You don't have enough coins.")
                else:
                    print("Invalid command. Please type '1', '2', or 'exit'.") #gpt yazdı marketin çoğunu
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