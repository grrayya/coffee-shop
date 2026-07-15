from cafe import Cafe

def run_game():
    game = Cafe()
    
    actions = {
        "1": lambda: print(f"Inventory: {game.inv.stock}"),
        "2": lambda: game.order_drink("Latte", "Arabica", "Oat"),
        "3": lambda: game.sell_sweet("Kalo Jam"),
        "q": exit
    }

    print("--- Cafe Management System ---")
    while True:
        print("\nOptions: [1] Status [2] Brew [3] Sell Sweet [q] Quit")
        cmd = input("Select an option: ").lower()
        
        if cmd in actions:
            actions[cmd]()
            game.save_state()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    run_game()
