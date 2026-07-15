import json
import os
from models import Drink, Sweet
from inventory import CafeInventory
from machines import BrewingUnit

class Cafe:
    def __init__(self):
        self.inv = CafeInventory()
        self.machine = BrewingUnit()
        self.revenue = 0
        self.day = 1
        self.load_save()

    def order_drink(self, name, beans, milk):
        if self.inv.consume_coffee_supplies():
            shot = self.machine.brew_espresso()
            self.revenue += 5.0
            return Drink(name, 5.0, beans, milk)
        print("Insufficient supplies for coffee")

    def sell_sweet(self, name):
        if self.inv.reduce_sweet_stock(name):
            self.revenue += 2.5
            return Sweet(name, 2.5)
        print(f"{name} is sold out")

    def end_day(self):
        print(f"Day {self.day} complete. Total revenue: ${self.revenue}")
        self.day += 1
        self.save_state()

    def save_state(self):
        with open('save.json', 'w') as f:
            json.dump({'stock': self.inv.stock, 'revenue': self.revenue, 'day': self.day}, f)

    def load_save(self):
        if os.path.exists('save.json'):
            with open('save.json', 'r') as f:
                state = json.load(f)
                self.inv.stock = state['stock']
                self.revenue = state['revenue']
                self.day = state['day']
