import json
import os

class Cafe:
    def __init__(self, data_file='cafe_save.json'):
        self.data_file = data_file
        self.inv = CafeInventory()
        self.machine = BrewingUnit()
        self.revenue = 0
        self.load_state()

    def save_state(self):
        data = {
            'inventory': self.inv.stock,
            'ingredients': self.inv.ingredients,
            'revenue': self.revenue
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f)

    def load_state(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.inv.stock = data['inventory']
                self.inv.ingredients = data['ingredients']
                self.revenue = data['revenue']

    # After any order_drink or sell_sweet, call self.save_state()
