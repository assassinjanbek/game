import random
from Player import Player

class Event:
    def __init__(self, player: Player):
        self.player = player
        self.event_no = random.randint(1,3)

    def start_event(self):
        if self.event_no == 1:
            print("\nYou took a nap under a tree, it was refreshing.\n")
            self.player.heal(5)
            print("\nYou've recovered \033[91m5 hp\033[0m.")

        if self.event_no == 2:
            print("\nYou found a coin! You are so lucky!\nOh wait, it was just a shiny rock.\n")

        if self.event_no == 3:
            print("\nYou are surrounded by a group of good looking creatures who claim to work for the Dungeon Master.\n\n"
                  "They said \033[93m'Roll one of your dice or toss a coin to see what will be happen next.'\033[0m\nYou were confused " \
                  "but you still did what they said.\n")
            value = self.roll_your_dice()
            print(f"You rolled \033[95m{value}\033[0m\n")
            if 0 < value < 3:
                print("They said \033[93m'You are in a miserable situation, we pity you.'\033[0m and they faded away in silence.\n")

            elif 2 < value < 6:
                print("They said \033[93m'Not bad, take this die, it will help you'\033[0m.\n" \
                "You took the die, it's a \033[95m12\033[0m sided die.\n")
                self.player.gain_dice(1, 12)
                print("They faded away in silence.\n")

            elif 5 < value < 10:
                print("They said \033[93m'You are one of the lucky ones, you deserve a prize.'\033[0m and they created a shiny object\n" \
                "You took the shiny object, when you took it, you felt a weird tingling, apparently it was a 20 sided dice.")
                self.player.heal(4)
                self.player.gain_dice(1, 20)
                print("\nYou've recovered \033[91m4 hp\033[0m.\n")
                print("They faded away in silence.\n")

            elif 9 < value < 17:
                print("They seemed to be impressed by what you did, they created a chest just in front of you.\nNow you are" \
                "way more impressed than them.\n" \
                "You opened the chest, there were dices and coins in it.")
                self.player.gain_coin(10)
                self.player.gain_dice(3, 6)
                self.player.gain_dice(3, 8)
                self.player.gain_dice(3, 10)
                print("\nYou've obtained \033[93m10 coin\033[0m; \033[95m3, 6\033[0m sided dice, \033[95m3, 8\033[0m sided dice and \033[95m3, 10\033[0m sided dice\n")
                print("They faded away in silence.\n")

            else:
                print("They looked shocked by what you did, and knelt before you. \033[93m'Please accept this gift precious player.'\033[0m\n" \
                "One of the creatures started to shine, you've get closer and closer to him. You felt a highly concentrated energy on you.\n" \
                "The shiny one has evaporated dramatically. Others slowly faded away in silence.\n\n" \
                "You've gained \033[91m10 maximum health\033[0m and healed up to your \033[91mmax health\033[0m.\n" \
                "While continuing your journey, you noticed that you have \033[95m10, 20\033[0m sided dice in your inventory.\n")
                self.player.gain_max_hp(10)
                self.player.hp = self.player.max_hp
                self.player.gain_dice(10, 20)


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
        
