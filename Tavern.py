from Player import Player

class Tavern:
    def __init__(self, player: Player):
        self.player = player

    def enter_tavern(self):

        print("\nWhat a cozy tavern!")

        tvrn = True
        while tvrn:
            print(self.player.general_info(), end="")
            if self.player.hp == self.player.max_hp:
                print("Your \033[91mhealth\033[0m is full.\n\n"
                "[1] Take an additional beer (give 2 coins)\n"
                "[2] Left the tavern (exit)")

                inp = input("(1/2): ")

                if inp == "1":         
                    _ = self.player.spend_coin(2)
                    if _ == 0:
                        print("\nYou don't have enough coin, even for a beer...")
                        continue
                    else:
                        self.player.heal(3)
                    print("\nBeer is as cold as your enemmies blood. You liked it.")

                elif inp == "2":
                    tvrn = False
                    print("\nYou are leaving from this cozy tavern\n")
                
                else:
                    print("\nPlease enter a reasonable number.")
                
            else:
                print("What would you do?\n\n"
                "[1] Take a beer (give \033[93m2 coins\033[0m => heal \033[91m3 hp\033[0m)\n"
                "[2] Eat a meal (give \033[93m6 coins\033[0m => heal \033[91m12 hp\033[0m)\n"
                "[3] Loan a room (give \033[93m20 coins\033[0m => heal to your \033[91mmax hp\033[0m)\n"
                "[4] Left the tavern (exit)")

                inp = input("(1/2/3/4): ")

                if inp == "1":
                    _ = self.player.spend_coin(2)
                    if _ == 0:
                        print("\nYou don't have enough coin, even for a beer...")
                        continue
                    else:
                        self.player.heal(3)
                    print("\nBeer is as cold as your enemmies blood. You liked it.")
                elif inp == "2":
                    _ = self.player.spend_coin(6)
                    if _ == 0:
                        print("\nYou don't have enough coins.")
                        continue
                    else:
                        self.player.heal(12)
                    print("\nYou really apreciated the meal.")
                elif inp == "3":
                    _ = self.player.spend_coin(20)
                    if _ == 0:
                        print("\nDid you really thinked that these will be enough for a room? Go find somewhere else!")
                        continue
                    else:
                        self.player.hp = self.player.max_hp
                    print("\nThe bed was decent, and it's better than outside. You felt refreshed.")
                elif inp == "4":
                    tvrn = False
                    print("\nYou are leaving from this cozy tavern\n")
                else:
                    print("\nPlease enter a reasonable number.")
                

    