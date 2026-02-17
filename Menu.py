# import sys
# from ColoredText import printcolor
# from Player import Player

# def menu(player: Player):

#     print("Welcome to the Project J!")

#     while True:
#         printcolor("Start the adventure? (yes/no/info)", "white")
#         ans = input()
#         if ans == "yes":
#             printcolor("\nLet's begin! Choose your character.\n\n", "cyan")
#             print(
#             "1) Dice Wizard 🎲 \nHe is the wizard of wizards and very familiar with dices.\n"
#             "Starts with:\n    6 six sided dice / 6 ten sided dice / 35 health\n"
#             "'Sometimes, a single die is enough to create a new destiny' -Dice Wizard\n\n"
#             "2) Gambler Wizard ♠️\nShe is one of the most dangerous beings in these lands and very familiar with coins.\n"
#             "'The probability of the numbers on the dice remains the same, of course, if you cannot control them.' -Gambler Wizard\n"
#             "Starts with:\n    15 six sided dice / 10 coins / 40 health")
#             while True:
#                 choice = input()
#                 if choice == "1":
#                     printcolor("You chose Dice Wizard.\n", "blue")
#                     player.character = "Dice Wizard"
#                     return
#                 elif choice == "2":
#                     printcolor("You chose Gambler Wizard.\n", "magenta")
#                     player.character = "Gambler Wizard"
#                     return
#         elif ans == "no":
#             print("ok bye!")
#             sys.exit()
#         elif ans == "info":
#             print("Project J:\n\n"
#             "Project J is a simple, luck and strategy based game.\n"
#             "All you have to do is choosing a wizard, and going trough an extraordinary adventure.\n\n"
#             "How to play:\n\n"
#             "During your adventure, you'll face up with many different things,\n"
#             "One of them is strange enemmies. When you encounter with an enemy, you have two different option.\n"
#             "You can choose an item (probably a dice) from your inventory or your can toss a coin.\n"
#             "If you desire to use your first item, you should type 1, and similarly 2 for your second item.\n"
#             "If you desire to toss a coin, which counts as a two sided dice, you should simply type 'coin' (you will lose a coin).\n"
#             "I think you should explore the rest of the game by yourself. Have fun!\n")
