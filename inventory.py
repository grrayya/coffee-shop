class CafeInventory:
    def __init__(self):
        self.stock = {'Kalo Jam': 12, 'Kachagolla': 20, 'Sandesh': 15, 'Mishti Doi': 8}
        self.ingredients = {'beans': 500, 'milk': 2000}

    def use_ingredients(self, beans_needed, milk_needed):
        if self.ingredients['beans'] < beans_needed or self.ingredients['milk'] < milk_needed:
            return False
        self.ingredients['beans'] -= beans_needed
        self.ingredients['milk'] -= milk_needed
        return True
