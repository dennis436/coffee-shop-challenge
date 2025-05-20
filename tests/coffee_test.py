import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_has_name():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_coffee_name_validation_and_immutability():
    with pytest.raises(Exception):
        Coffee(123)
    with pytest.raises(Exception):
        Coffee("AB")  # less than 3 chars

    coffee = Coffee("Mocha")
    with pytest.raises(Exception):
        coffee.name = "Latte"

def test_coffee_orders_and_customers():
    coffee = Coffee("Cappuccino")
    customer = Customer("Ana")
    customer.create_order(coffee, 5.5)
    assert len(coffee.orders()) == 1
    assert customer in coffee.customers()

def test_num_orders_and_avg_price():
    coffee = Coffee("Drip")
    customer = Customer("Ben")
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 7.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 6.0
