import Character
import Menu

def game():
    player = Menu.menu()
    player = Character.character(player)
    print(player)

game()


