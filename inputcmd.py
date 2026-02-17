# bunu sallamasyon yazdım, yes no info falan onları toptan ayarlamak lazım ayrı ayrı olmaz
#şarjımbitiyor

import sys


def inputcmd(prompt=""):
    print(prompt, end="")
    cmd = input("\n> ").lower().strip()
    return cmd
#     if cmd in ["1", "2", "3", "4", "5", "6", "yes", "no", "info"]:
#         return cmd
#     #elif cmd == "coin":
#     #    Events.coin_toss()
#     elif cmd == "help":
#         print("You can enter the number of the die you want to use or 'coin' to toss a coin.")
#         inputcmd()
#     elif cmd == "exit":
#         print("Exiting the game. Goodbye!")
#         sys.exit()
#     elif cmd == "inventory":
#         print("Your inventory:")
#         # you would typically call a method to display the player's inventory
#         inputcmd()
#     elif cmd == "status":
#         print("Your status:")
#         # aynı şekilde
#         inputcmd()
#     elif cmd == "score":
#         #print(f"Your score is: {player.score}")
#         inputcmd()
#     else:
#         print("Invalid command. Please try again.")
#         return inputcmd()
# #    elif: cmd == "shop":
# #        Shop.enter_shop(player)