import Character
import Menu
import GameLoop
import Win

def game():
    player_name = Menu.menu()
    player = Character.character(player_name)
    print(player.general_info())
    GameLoop.loop(player)
    Win.winning(player)

game()