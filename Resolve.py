from Combat import Combat
import Enemy_selection

def resolve(str, player):
    print("hello")
    if str == "Merciful Enemy":
        enemy = Enemy_selection.select_enemy()
        combat = Combat(enemy, player)
        combat.start_combat()
    elif str == "Cruel Enemy":
        enemy = Enemy_selection.select_enemy()
        combat = Combat(enemy, player)
        combat.start_combat()
    elif str == "Tavern":
        print("Take a rest")
    elif str == "Event":
        print("What?!? an event?!?!")
    elif str == "Market":
        print("Senin paran burada geçmez kardeşim.")
