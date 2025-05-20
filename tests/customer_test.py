
import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.latte = Coffee("Latte")

    def test_valid_name(self):
        self.assertEqual(self.customer.name, "Alice")

    def test_invalid_name_raises(self):
        with self.assertRaises(ValueError):
            Customer("")

        with self.assertRaises(ValueError):
            Customer("x" * 16)

        with self.assertRaises(ValueError):
            self.customer.name = 123

    def test_create_order(self):
        order = self.customer.create_order(self.latte, 5.0)
        self.assertEqual(len(self.customer.orders()), 1)
        self.assertEqual(order.coffee, self.latte)

    def test_coffees(self):
        self.customer.create_order(self.latte, 4.0)
        self.customer.create_order(self.latte, 4.5)
        self.assertEqual(self.customer.coffees(), [self.latte])

if __name__ == '__main__':
    unittest.main()
