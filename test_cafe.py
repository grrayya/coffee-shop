import unittest
from cafe import Cafe

class TestCafe(unittest.TestCase):
    def setUp(self):
        self.shop = Cafe()

    def test_drink_brewing(self):
        initial_revenue = self.shop.revenue
        self.shop.order_drink("Latte", "Arabica", "Oat")
        self.assertTrue(self.shop.revenue > initial_revenue)

    def test_sweet_sale(self):
        initial_stock = self.shop.inv.stock['Kalo Jam']
        self.shop.sell_sweet('Kalo Jam')
        self.assertEqual(self.shop.inv.stock['Kalo Jam'], initial_stock - 1)

    def test_insufficient_ingredients(self):
        # Empty the stock manually to test failure
        self.shop.inv.ingredients = {'beans': 0, 'milk': 0}
        result = self.shop.order_drink("Latte", "Arabica", "Oat")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
