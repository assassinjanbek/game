import Character
import Menu
import Enemy_selection
import Combat

def game():
    player = Menu.menu()
    player = Character.character(player)
    print(player)
    enemy = Enemy_selection.select_enemy()
    combat = Combat.Combat(enemy, player)
    combat.start_combat()
    print(player)

game()