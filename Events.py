from Player import Player


def use_item(args, player: Player):
    if not args:
        print("Use what? Try: " "\033[90muse <number>\033[0m" " or " "\033[90muse coin\033[0m")
        return

    target = args[0]

    if target == "coin":
        value = player.toss_a_coin()
        print(f"You tossed a \033[93mcoin\033[0m! 🪙")
        return value

    if not target.isdigit():
        print("Please enter a number (e.g., 1 for your first item) or 'coin'.")
        return

    if int(target) < 1 or int(target) >= len(player.inventory):
        print("Please enter a valid number for your inventory item.")
        return

    die = player.inventory[int(target) - 1]
    value = die.rolling()
    if die.quantity == 0:
        player.inventory.remove(die)
    print(f"You rolled {value} using your die.")
