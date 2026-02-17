from enum import Enum, auto
from Player import Player
from Enemy_selection import select_enemy
from ColoredText import printcolor

# Enum sadece okumayı kolaylaştıran bir şey, GameState.START 0 demek, GameState.MENU 1 demek, normal 0, 1, 2, 3'ten farkı yok, 
# yani if bloğunda şu oluyor: game.state = 1 ise menüyü aç, game.state = 2 ise exploring yaz gibi, game.state normal int aslında
class GameState(Enum): 
    START = 0
    MENU = 1
    EXPLORING = 2
    COMBAT = 3
    GAME_OVER = 4

class Game:
    def __init__(self):
        self.state = GameState.START
        self.running = True
        self.player = Player()
        self.current_enemy = None


    # Game class'ı oyunu çalışyırıyor, bu şekilde game class'ına özel variable'lar yapıp istediğim yerde kullanabiliyorum, 
    # mesela player'ı burada tanımladım
    def run(self):
        print("Welcome to the Project J!")

        # Ana loop, sadece bu üç şey döndürüyor oyunu
        while self.running:
            self.render_hud() # ekrana gelcek şeyi burda basıyorum, ilerde sabit yazılar yapılabilir bu şekilde
            cmd = input("\n").strip().lower() # input normal
            import CommandHandler # bunu buraya chatgpt yazdırdı, circular import oluyormuş çözemedim, uğraşmadım daha doğrusu
            CommandHandler.handle_command(cmd, self) # komutları buraya attım, orda ilgilendim tamamen


    # Bu fonksiyon ekrana gelicek şeyleri basıyor, böyle bir fonksiyon yerine CommandHandler'da her komutun sonunda print de yapabilirdim
    # ama böyle daha ileriye dönük, böyle hem komutlar da basılabilir combat seçenekleri gibi, ekranda sabit kalcak şeyler de basılabilir
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
            printcolor("You are exploring the world...", "yellow")
            
        
        if self.state == GameState.COMBAT:
            printcolor(f"You've encountered a {self.current_enemy.name}!", "red")

        if self.state == GameState.GAME_OVER:
            printcolor("You are dead. Sorry.（＞人＜；）", "red")
            print("score: " + str(self.player.score))