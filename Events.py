import random
from Player import Player
import sys
from Combat import Combat
from Enemy import Enemy
from Dice import Dice

class Event:
    def __init__(self, player: Player):
        self.player = player
        self.event_no = random.randint(1,4)

    def start_event(self):
        if self.event_no == 1:
            print("\nYou took a nap under a tree, it was refreshing.")
            self.player.heal(4)
            print("\nYou've recovered \033[91m4 hp\033[0m.")
            print(self.player.general_info())

        if self.event_no == 2:
            _ = random.randint(1,2)
            if _ == 1:
                print("\nYou found a \033[93mcoin\033[0m! You are so lucky!\nOh wait, it was just a shiny rock.")
            if _ == 2:
                print("\nYou found a \033[93mcoin\033[0m! You are so lucky!")
                self.player.gain_coin(1)
            print(self.player.general_info())

        if self.event_no == 3:
            print("\nYou are surrounded by a group of good looking creatures who claim to work for the Dungeon Master.\n\n"
                  "They said \033[93m'Roll one of your dice or toss a coin to see what will be happen next.'\033[0m\nYou were confused " \
                  "but you still did what they said.")
            value = self.roll_your_dice()
            print(f"You rolled \033[95m{value}\033[0m\n")
            if 0 < value < 3:
                print("They said \033[93m'You are in a miserable situation, we pity you.'\033[0m and they faded away in silence.")

            elif 2 < value < 6:
                print("They said \033[93m'Not bad, take this die, it will help you'\033[0m.\n" \
                "You took the die, it's a \033[95m12\033[0m sided die.\n")
                self.player.gain_dice(1, 12)
                print("They faded away in silence.")

            elif 5 < value < 10:
                print("They said \033[93m'You are one of the lucky ones, you deserve a prize.'\033[0m and they created a shiny object\n" \
                "You took the shiny object, when you took it, you felt a weird tingling, apparently it was a \033[95m20\033[0m sided dice.")
                self.player.heal(4)
                self.player.gain_dice(1, 20)
                print("\nYou've recovered \033[91m4 hp\033[0m.\n")
                print("They faded away in silence.")

            elif 9 < value < 17:
                print("They seemed to be impressed by what you did, they created a chest just in front of you.\nNow you are" \
                "way more impressed than them.\n" \
                "You opened the chest, there were dices and coins in it.")
                self.player.gain_coin(10)
                self.player.gain_dice(3, 6)
                self.player.gain_dice(3, 8)
                self.player.gain_dice(3, 10)
                print("\nYou've obtained \033[93m10 coin\033[0m; \033[95m3, 6\033[0m sided dice, \033[95m3, 8\033[0m sided dice and \033[95m3, 10\033[0m sided dice\n")
                print("They faded away in silence.")

            else:
                print("They looked shocked by what you did, and knelt before you. \033[93m'Please accept this gift precious player.'\033[0m\n" \
                "One of the creatures started to shine, you've get closer and closer to him. You felt a highly concentrated energy on you.\n" \
                "The shiny one has evaporated dramatically. Others slowly faded away in silence.\n\n" \
                "You've gained \033[91m10 maximum health\033[0m and healed up to your \033[91mmax health\033[0m.\n" \
                "While continuing your journey, you noticed that you have \033[95m10, 20\033[0m sided dice in your inventory.")
                self.player.gain_max_hp(10)
                self.player.hp = self.player.max_hp
                self.player.gain_dice(10, 20)
            
            print(self.player.general_info())

        if self.event_no == 4:
            print("\nYou saw a cave enterance, it's covered by webs and looks terrifying. Do you really want to go inside?\n\n" \
            "[1] Yes.\n" \
            "[2] Hell no. (You coward.)")
            loop = True
            while loop:
                _ = input("(1/2): ")
                if _ == "1":
                    loop = False
                    print("\nYou've entered the cave, there are cloths and armors everywhere, you've heard some voices. Do you really want to go deeper?\n\n" \
                    "[1] Hell yeah.\n" \
                    "[2] No. (You coward)")
                    l = True
                    while l:
                        _ = input("(1/2): ")
                        if _ == "1":
                            l = False
                            print("\n You went deeper and have encountered with an old spider-lady! Apparently, she is knitting something.\n\n" \
                            "'Oh hi dear! Come on sit, tell me, do you need something?' she said.\n\n" \
                            "[1] 'Yeah, I am very fragile for this cruel world, do you have something for me?'\n" \
                            "[2] 'Yeah, I am getting out of dice, do you have some dice?'\n" \
                            "[3] 'Yeah, I want your little soul, you monster!'\n")
                            _ = input("(1/2/3): ")
                            if _ == "1":
                                print("\n'What a coincidence my little one! You can take this webby armor that I just knitted.' she said.")
                                self.player.gain_max_hp(5)
                                print("\nYou've gained \033[91m5 max hp\033[0m from that armor.")
                                print(self.player.general_info())

                            elif _ == "2":
                                print("\n'You may take this webby dice bag then my darling' she said.\n When you took the bag, it exploded and plenty" \
                                "of dice fell into your hand.")
                                self.player.gain_dice(1,4)
                                self.player.gain_dice(1,6)
                                self.player.gain_dice(1,8)
                                self.player.gain_dice(1,10)
                                self.player.gain_dice(1,12)
                                self.player.gain_dice(1,20)
                                print("\nYou've gained \033[95ma dice set\033[0m.")
                                print(self.player.general_info())
                                
                            else:
                                print("She become furious istantly, you've started to fight under the moonlight.")
                                enemy = Enemy(Dice(8, 8), 5, 25, "Spider Lady", "\033[91m")
                                combat = Combat(enemy, self.player)
                                combat.start_combat()
                                print("\n You also took the webby armor she was knitting.")
                                self.player.gain_max_hp(5)
                                print("\nYou've gained \033[91m5 max hp\033[0m from that armor.")
                                print(self.player.general_info())


                        elif _ == "2":
                            print("\nYou get away from the cave but your curiosity hurt you\n")
                            self.player.take_damage(5)
                            if self.player.hp < 1:
                                print("You are \033[91mdead.\033[0m Sorry.（＞人＜；）")
                                sys.exit()
                            else:
                                print("You took \033[91m5\033[0m damage\n")
                                l = False
                        else:
                            print("\nEnter a valid number")
                elif _ == "2":
                    print("\nYou get away from the cave but your curiosity hurt you\n")
                    self.player.take_damage(3)
                    if self.player.hp < 1:
                        print("You are \033[91mdead.\033[0m Sorry.（＞人＜；）")
                        sys.exit()
                    else:
                        print("You took \033[91m3\033[0m damage\n")
                        loop = False

                else:
                    print("\nEnter a valid number")

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
        
