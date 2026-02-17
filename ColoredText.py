def printcolor(text, color):
    colors = {
        "grey": "\033[90m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m" # Reset color after printing
    }
    print(f"{colors.get(color, colors['reset'])}{text}{colors['reset']}") # colors'dan color'ı al, yoksa reset kullan

def inputcolor(prompt, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    return input(f"{colors.get(color, colors['reset'])}{prompt}{colors['reset']}")

# Example 