from Combat import Combat
import Enemy_selection
from Tavern import Tavern
from Market import Market
from Events import Event

def resolve(room, player):
    if room == "Merciful Enemy":
        enemy = Enemy_selection.select_merciful_enemy()
        combat = Combat(enemy, player)
        combat.start_combat()

    elif room == "Cruel Enemy":
        enemy = Enemy_selection.select_cruel_enemy()
        combat = Combat(enemy, player)
        combat.start_combat()

    elif room == "Tavern":
        tavern = Tavern(player)
        tavern.enter_tavern()

    elif room == "Event":
        event = Event(player)
        event.start_event()

    elif room == "Market":
        market = Market(player)
        market.enter_market()

    elif room == "Boss":
        print("You've encountered a mighty enemy.")
        enemy = Enemy_selection.select_boss()
        combat = Combat(enemy, player)
        combat.start_combat()