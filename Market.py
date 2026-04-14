from Player import Player
from Dice import Buyable_Dice

class Market:
    def __init__(self, player: Player):
        self.player = player

    def enter_market(self):

        print("You entered to the weird looking market. Shopkeeper has a weird look.")
        mrkt = True

        while mrkt:
            d4 = Buyable_Dice(4, 5, 3)
            d6 = Buyable_Dice(6, 3, 5)
            d8 = Buyable_Dice(8, 3, 8)
            d10 = Buyable_Dice(10, 2, 12)
            d12 = Buyable_Dice(12, 2, 15)
            d20 = Buyable_Dice(20, 1, 25)
            print("What would you do?\n\n"
            "[1] Buy something\n"
            "[2] Sell something\n"
            "[3] Left the market\n"
            )

            inp = input("(1/2/3): ")

            if inp == "1":
                buy = True
                while buy:
                    print(f"\n[1] {d4.quantity}x d4 ({d4.price} coins)\n"
                    f"[2] {d6.quantity}x d6 ({d6.price} coins)\n"
                    f"[3] {d8.quantity}x d8 ({d8.price} coins)\n"
                    f"[4] {d10.quantity}x d10 ({d10.price} coins)\n"
                    f"[5] {d12.quantity}x d12 ({d12.price} coins)\n"
                    f"[6] {d20.quantity}x d20 ({d20.price} coins)\n"
                    "[7] Go back"
                    )
                    buy_inp = input("(1/2/3/4/5/6): \n")

                    if buy_inp == "1":
                        _ = self.player.spend_coin(d4.price)
                        if _ == 0:
                            continue
                        else:
                            d4.price += 1
                            d4.quantity -= 1
                            self.player.buying_die(4)

                    elif buy_inp == "2":
                        _ = self.player.spend_coin(d6.price)
                        if _ == 0:
                            continue
                        else:
                            d6.price += 1
                            d6.quantity -= 1
                            self.player.buying_die(6)

                    elif buy_inp == "3":
                        _ = self.player.spend_coin(d8.price)
                        if _ == 0:
                            continue
                        else:
                            d8.price += 1
                            d8.quantity -= 1
                            self.player.buying_die(8)

                    elif buy_inp == "4":
                        _ = self.player.spend_coin(d10.price)
                        if _ == 0:
                            continue
                        else:
                            d10.price += 1
                            d10.quantity -= 1
                            self.player.buying_die(10)

                    
                    elif buy_inp == "5":
                        _ = self.player.spend_coin(d12.price)
                        if _ == 0:
                            continue
                        else:
                            d12.price += 1
                            d12.quantity -= 1
                            self.player.buying_die(12)


                    elif buy_inp == "6":
                        _ = self.player.spend_coin(d20.price)
                        if _ == 0:
                            continue
                        else:
                            d20.price += 1
                            d20.quantity -= 1
                            self.player.buying_die(20)

                    elif buy_inp == "7":
                        buy = False
                        
                    else:
                        print("please enter a reasonable number")

            elif inp == "2":
                no = input(f"You have {self.player.coin} coin\n{self.player.dice_info()}\nChoose a dice from your inventory to sell: ").strip()
                if 0 <= int(no) - 1 < len(self.player.inventory):
                    die = self.player.inventory[int(no) - 1]
                    die.quantity -= 1
                    self.player.gain_coin((die.side)//2)
                    print(f"You gained {(die.side)//2} coin")
                    if die.quantity == 0:
                        self.player.inventory.remove(die)
                else:
                    print("Please enter a valid number. (For example, 1 for your first die)")

            elif inp == "3":
                mrkt = False
                print("You are leaving from this weird looking market")


                        
