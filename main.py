from cafe import Cafe

def main():
    shop = Cafe()
    
    while True:
        print(f"\nDay {shop.day} | ${shop.revenue}")
        print("1: Brew | 2: Sell Sweet | 3: Status | 4: End Day | q: Exit")
        choice = input("> ")

        if choice == "1":
            shop.order_drink("Latte", "Arabica", "Oat")
        elif choice == "2":
            shop.sell_sweet("Kalo Jam")
        elif choice == "3":
            print(shop.inv.stock)
        elif choice == "4":
            shop.end_day()
        elif choice == "q":
            break

if __name__ == "__main__":
    main()
