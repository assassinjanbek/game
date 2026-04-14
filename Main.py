import Character
import Menu
import GameLoop

def game():
    player_name = Menu.menu()
    player = Character.character(player_name)
    print(player)
    GameLoop.loop(player)
    print("Congrats! You beat the boss! YOU won the game!")

game()