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
        print(f"\nYou bought {q}, {d} sided dice.")

    def enter_market(self):

        print("\nYou entered to the weird looking market. Shopkeeper has a weird look.")
        mrkt = True

        dices = [4, 6, 8, 10, 12, 20]
        chosen_dices = random.sample(dices, k=3)
        quantities = random.choices(range(3,10), k=3)

        while mrkt:
            
            print("\nWhat would you do?\n\n"
            "[1] Buy something\n"
            "[2] Sell something\n"
            "[3] Left the market\n"
            )

            inp = input("(1/2/3): ")

            if inp == "1":
                
                prices = []
                t = 4
                for _ in range(3):
                    prices.append(((chosen_dices[_])*(quantities[_]))//t)        

                buy = True
                bought_1 = 0
                bought_2 = 0
                bought_3 = 0
                offer_1 = f"[1] {quantities[0]}x d{chosen_dices[0]} ({prices[0]} coins)\n"
                offer_2 = f"[2] {quantities[1]}x d{chosen_dices[1]} ({prices[1]} coins)\n"
                offer_3 = f"[3] {quantities[2]}x d{chosen_dices[2]} ({prices[2]} coins)\n"
                while buy:
                    if bought_1 == 1:
                        offer_1 = "[1] Owned\n"
                    if bought_2 == 1:
                        offer_2 = "[2] Owned\n"
                    if bought_3 == 1:
                        offer_3 = "[3] Owned\n"

                    print(self.player.general_info(), end="")
                    print(f"{offer_1}{offer_2}{offer_3}[4] Go back")

                    buy_inp = input("(1/2/3/4): ")

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
                            print("You already bought that.")

                    elif buy_inp == "4":
                        buy = False
                        
                    else:
                        print("\nplease enter a reasonable number")

            elif inp == "2":
                no = input(f"{self.player.general_info()}"
                           "You will gain approximately 1/3 coin of your die's side number\n"
                            "Choose a dice from your inventory to sell: ").strip()

                if not no.isdigit():
                    print("Please enter a number.")
                    continue

                if 0 <= int(no) - 1 < len(self.player.inventory):
                    die = self.player.inventory[int(no) - 1]
                    die.quantity -= 1
                    self.player.gain_coin((die.side)//3)
                    print(f"\nYou gained {(die.side)//3} coin")
                    if die.quantity == 0:
                        self.player.inventory.remove(die)

                else:
                    print("\nPlease enter a valid number. (For example, 1 for your first die)")

            elif inp == "3":
                mrkt = False
                print("\nYou are leaving from this weird looking market\n")


                        
