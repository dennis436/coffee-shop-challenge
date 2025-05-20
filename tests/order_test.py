import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Charlie")
        self.coffee = Coffee("Americano")

    def test_order_creation(self):
        order = Order(self.customer, self.coffee, 6.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 6.5)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)

        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            Order("NotCustomer", self.coffee, 5.0)

        with self.assertRaises(TypeError):
            Order(self.customer, "NotCoffee", 5.0)

if __name__ == '__main__':
    unittest.main()