import random
from Player import Player
from Dice import Dice

class Event:
    def __init__(self, player: Player):
        self.player = player
        self.event_no = random.randint(1,3)

    def start_event(self):
        if self.event_no == 1:
            print("\nYou took a nap under a tree, it was refreshing.")
            self.player.heal(5)

        if self.event_no == 2:
            print("\nYou found a coin! you are so lucky! oh wait, it was just a shiny rock.")

        if self.event_no == 3:
            print("\nYou are surrounded by a group of creepy creatures who claim to work for the Dungeon Master.\n\n"
                  "They said 'Roll one of your dice or toss a coin to see what will be happen next.'\n You were confused" \
                  "but you still did what they said.\n")
            value = self.roll_your_dice()
            if 0 < value < 3:
                print("You are in a miserable situation")
            elif 2 < value < 6:
                print("")
            elif 5 < value < 10:
                print("")
            elif 9 < value < 15:
                print("")
            else:
                print("")

    def roll_your_dice(self):
         while True:
            no = input(f"{self.player.general_info()}"
                       f"Choose a die from your inventory: ").strip()
            if no == "c":
                value = self.player.toss_a_coin()
                if value == 0:
                    continue
                else:
                    return value
            elif not no.isdigit():
                print("\nPlease enter a number.")
                continue

            if 0 <= int(no) - 1 < len(self.player.inventory):
                die = self.player.inventory[int(no) - 1]
                value = die.rolling()
                return value
            else:
                print("\nPlease enter a valid number. (For example, 1 for your first die)")
        
