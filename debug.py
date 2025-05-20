from customer import Customer
from coffee import Coffee

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")
charlie = Customer("Charlie")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")
mocha = Coffee("Mocha")

# Create orders
alice.create_order(latte, 4.5)
alice.create_order(mocha, 5.0)
bob.create_order(latte, 6.0)
charlie.create_order(latte, 3.5)
charlie.create_order(mocha, 4.0)
charlie.create_order(espresso, 2.5)

# Test Customer.orders()
print("\n🧾 Orders for Alice:")
for order in alice.orders():
    print(f"  {order.coffee.name} - ${order.price}")

# Test Customer.coffees()
print("\n☕ Coffees ordered by Charlie:", [c.name for c in charlie.coffees()])

# Test Coffee.orders()
print("\n📋 Orders for Latte:")
for order in latte.orders():
    print(f"  {order.customer.name} - ${order.price}")

# Test Coffee.customers()
print("\n👥 Customers who ordered Mocha:", [c.name for c in mocha.customers()])

# Test Coffee.num_orders() and average_price()
print(f"\n📊 Latte orders count: {latte.num_orders()}")
print(f"💰 Latte average price: ${latte.average_price():.2f}")

# Test most_aficionado()
most_spent = Customer.most_aficionado(latte)
if most_spent:
    print(f"\n🏆 Most aficionado of Latte: {most_spent.name}")
else:
    print("\n🏆 No orders for this coffee yet.")