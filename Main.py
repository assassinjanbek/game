import Character
import Menu
import GameLoop

def game():
    player_name = Menu.menu()
    player = Character.character(player_name)
    print(player)
    GameLoop.loop(player)
    print("Congrats! you won the game!")

game()