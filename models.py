from abc import ABC

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Drink(Product):
    def __init__(self, name, price, bean_type, milk_type):
        super().__init__(name, price)
        self.bean_type = bean_type
        self.milk_type = milk_type

class Sweet(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
