from Player import Player

class Market:
    def __init__(self, player: Player):
        self.player = player

    def enter_market(self):

        print("You entered to the weird looking market. Shopkeeper has a weird look.")
        mrkt = True

        while mrkt:
            print("What would you do?\n\n"
            "[1] Buy something\n"
            "[2] Sell something\n"
            "[3] Left the market\n"
            )
