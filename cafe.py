from models import Drink, Sweet
from inventory import CafeInventory
from machines import BrewingUnit

class Cafe:
    def __init__(self):
        self.inv = CafeInventory()
        self.machine = BrewingUnit()

    def order_drink(self, name, beans, milk):
        if self.inv.use_ingredients(20, 50):
            shot = self.machine.brew()
            return Drink(name, 5.00, beans, milk)
        return None

    def sell_sweet(self, name):
        if self.inv.stock.get(name, 0) > 0:
            self.inv.stock[name] -= 1
            return Sweet(name, 2.50)
        return None
