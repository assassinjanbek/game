from Player import Player

class Tavern:
    def __init__(self, player: Player):
        self.player = player

    def enter_tavern(self):

        print("What a cozy tavern\n")
        tvrn = True
        while tvrn:
            print("What would you do?\n\n"
            "[1] Take a beer (give 2 coin => heal 3 hp)\n"
            "[2] Eat a meal (give 6 coin => heal 12 hp)\n"
            "[3] Loan a room (give 20 coin => heal to your max hp)\n"
            "[4] Left the tavern (exit)\n")

            inp = input("(1/2/3/4) : ")

            if inp == "1":
                _ = self.player.spend_coin(2)
                if _ == 0:
                    continue
                else:
                    self.player.heal(3)
                print("Beer is as cold as your enemmies blood. You liked it.\n")

            if inp == "2":
                _ = self.player.spend_coin(6)
                if _ == 0:
                    continue
                else:
                    self.player.heal(12)
                print("You really apreciate the meal.\n")

            if inp == "3":
                _ = self.player.spend_coin(20)
                if _ == 0:
                    continue
                else:
                    self.player.hp = self.player.max_hp
                print("The bed was decent, but it's better than outside. You felt refreshed.\n")

            if inp == "4":
                tvrn = False
                print("You are leaving from this cozy tavern\n")

            else:
                print("Please enter a reasonable number.\n")
                

    