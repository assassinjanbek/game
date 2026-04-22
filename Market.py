from Player import Player
import random
from Dice import Dice

class Market:
    def __init__(self, player: Player):
        self.player = player

    def buying_die(self, d, q):
        die_found = None
        for die in self.player.inventory:
            if die.side == d:
                die_found = die
                break
        if die_found:
            die_found.quantity += q
        else:
            self.player.inventory.append(Dice(d, q))
        print(f"\nYou bought \033[95m{q}, {d}\033[0m sided dice.")

    def enter_market(self):

        print("\nYou entered to the weird looking market. Shopkeeper has a weird look.")
        mrkt = True

        dices = [4, 6, 8, 10, 12, 20]
        chosen_dices = random.sample(dices, k=3)
        quantities = random.choices(range(3,10), k=3)
        bought_1 = 0
        bought_2 = 0
        bought_3 = 0

        while mrkt:
            
            print("\nWhat would you do?\n\n"
            "[1] Buy something\n"
            "[2] Sell something\n"
            "[3] Leave the market\n"
            )

            inp = input("(1/2/3): ")

            if inp == "1":
                
                prices = []
                t = 3.5
                for _ in range(3):
                    prices.append(round(((chosen_dices[_])*(quantities[_]))/t))

                buy = True

                offer_1 = f"[1] \033[95m{quantities[0]}, {chosen_dices[0]}\033[0m sided dice ({prices[0]} coins)\n"
                offer_2 = f"[2] \033[95m{quantities[1]}, {chosen_dices[1]}\033[0m sided dice ({prices[1]} coins)\n"
                offer_3 = f"[3] \033[95m{quantities[2]}, {chosen_dices[2]}\033[0m sided dice ({prices[2]} coins)\n"
                while buy:
                    if bought_1 == 1:
                        offer_1 = "[1] \033[96mOwned\033[0m\n"
                    if bought_2 == 1:
                        offer_2 = "[2] \033[96mOwned\033[0m\n"
                    if bought_3 == 1:
                        offer_3 = "[3] \033[96mOwned\033[0m\n"

                    print(self.player.general_info(), end="")
                    print(f"\n{offer_1}{offer_2}{offer_3}\n[0] Go back.")

                    buy_inp = input("(1/2/3/0): ")

                    if buy_inp == "1":
                        if bought_1 == 0:
                            _ = self.player.spend_coin(prices[0])
                            if _ == 0:
                                continue
                            else:
                                self.buying_die(chosen_dices[0], quantities[0])
                                bought_1 = 1
                        else:
                            print("You already bought that.")

                    elif buy_inp == "2":
                        if bought_2 == 0:
                            _ = self.player.spend_coin(prices[1])
                            if _ == 0:
                                continue
                            else:
                                self.buying_die(chosen_dices[1], quantities[1])
                                bought_2 = 1
                        else:
                            print("You already bought that.")

                    elif buy_inp == "3":
                        if bought_3 == 0:
                            _ = self.player.spend_coin(prices[2])
                            if _ == 0:
                                continue
                            else:
                                self.buying_die(chosen_dices[2], quantities[2])
                                bought_3 = 1
                        else:
                            print("\nYou already bought that.")

                    elif buy_inp == "0":
                        buy = False
                        
                    else:
                        print("\nplease enter a reasonable number")

            elif inp == "2":
                sell = True
                while sell:
                    no = input(f"{self.player.general_info()}"
                               "[0] Go back.\n\n"
                               "You will gain approximately 1/4 coin of your die's side number.\n\n"
                                "Choose a dice from your inventory to sell: ").strip()

                    if not no.isdigit():
                        print("Please enter a number.")
                        continue

                    elif 0 <= int(no) - 1 < len(self.player.inventory):
                        die = self.player.inventory[int(no) - 1]
                        die.quantity -= 1
                        self.player.gain_coin(round((die.side)/4))
                        print(f"\nYou gained \033[93m{round((die.side)/4)} coin\033[0m.")
                        if die.quantity == 0:
                            self.player.inventory.remove(die)

                    elif no == "0":
                        sell = False

                    else:
                        print("\nPlease enter a valid number. (For example, 1 for your first die)")

            elif inp == "3":
                mrkt = False
                print("\nYou are leaving from this weird looking market\n")


                        
