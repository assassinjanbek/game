from enum import Enum, auto
from Player import Player
from Enemy_selection import select_enemy
from ColoredText import printcolor

class GameState(Enum):
    START = auto()
    MENU = auto()
    EXPLORING = auto()
    COMBAT = auto()
    GAME_OVER = auto()

class Game:
    def __init__(self):
        self.state= GameState.START
        self.running = True
        self.player = Player()
        self.current_enemy = None


    def run(self):
        print("Welcome to the Project J!")

        # Ana loop, sadece bu üç şey dönüyor oyun boyu
        while self.running:
            self.render_hud() # ekrana gelcek şeyi burda basıyorum, ilerde sabit yazılar yapılabilir bu şekilde
            cmd = input("\n>> ").strip().lower() # input bildiğin
            import CommandHandler
            CommandHandler.handle_command(cmd, self) # komutları buraya attım


    def render_hud(self):

        if self.state == GameState.START:
            printcolor("Start the adventure? (yes/no/info)", "white")
            
        
        if self.state == GameState.MENU:
            printcolor("\nLet's begin! Choose your character.\n\n", "cyan")
            print(
            "1) Dice Wizard 🎲 \nHe is the wizard of wizards and very familiar with dices.\n"
            "Starts with:\n    6 six sided dice / 6 ten sided dice / 35 health\n"
            "'Sometimes, a single die is enough to create a new destiny' -Dice Wizard\n\n"
            "2) Gambler Wizard ♠️\nShe is one of the most dangerous beings in these lands and very familiar with coins.\n"
            "'The probability of the numbers on the dice remains the same, of course, if you cannot control them.' -Gambler Wizard\n"
            "Starts with:\n    15 six sided dice / 10 coins / 40 health")
            
        
        if self.state == GameState.EXPLORING:
            printcolor("\nYou are exploring the world...\n", "yellow")
            
        
        if self.state == GameState.COMBAT:
            printcolor(f"\nYou've encountered an {self.current_enemy.name}!\n", "red")

        if self.state == GameState.GAME_OVER:
            printcolor("\nYou are dead. Sorry.（＞人＜；）", "red")