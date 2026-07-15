class CafeInventory:
    def __init__(self):
        self.stock = {'Kalo Jam': 12, 'Kachagolla': 20, 'Sandesh': 15, 'Mishti Doi': 8}
        self.ingredients = {'beans': 500, 'milk': 2000}

    def consume_coffee_supplies(self):
        if self.ingredients['beans'] < 20 or self.ingredients['milk'] < 50:
            return False
        
        self.ingredients['beans'] -= 20
        self.ingredients['milk'] -= 50
        return True

    def reduce_sweet_stock(self, sweet_name):
        if self.stock.get(sweet_name, 0) > 0:
            self.stock[sweet_name] -= 1
            return True
        return False
