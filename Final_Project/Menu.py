import sys

def menu():

    print("Welcome to the Project J!")


    while True:
        ans = input("Start the adventure? (yes/no): ")
        if ans == "yes":
            print("Let's begin! Choose your character.\n"
            "1) Dice Wizard \n He is the wizard of wizards and very familiar with dices.\n"
            "Starts with:\n 6 six sided dice / 6 ten sided dice / 35 health\n"
            "'Sometimes, a single die is enough to create a new destiny' -Dice Wizard\n"
            "2) Gambler Wizard \n She is one of the most dangerous beings in these lands and very familiar with coins.\n"
            "'The probability of the numbers on the dice remains the same, of course, if you cannot control them.' -Gambler Wizard\n"
            "Starts with:\n 15 six sided dice / 10 coins / 40 health")
            while True:
                player = input("1/2: ")
                if player == "1":
                    print("You chose Dice Wizard.  ")
                    return "Dice Wizard"
                elif player == "2":
                    print("You chose Gambler Wizard. Nothing will be as it seems!")
                    return "Gambler Wizard"
        if ans == "no":
            print("ok bye!")
            sys.exit()