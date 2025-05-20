# ☕ Coffee Shop Challenge

A Python OOP project simulating customers, coffees, and orders in a coffee shop — built to demonstrate object relationships, data validation, and aggregate behavior.

---

## 📁 Project Structure

```
coffee-shop-challenge/
├── lib/
│   ├── customer.py       # Customer class
│   ├── coffee.py         # Coffee class
│   └── order.py          # Order class
├── tests/
│   ├── customer_test.py  # Unit tests for Customer
│   ├── coffee_test.py    # Unit tests for Coffee
│   └── order_test.py     # Unit tests for Order
├── debug.py              # Sample usage and debug output
└── README.md             # Project overview (this file)
```

---

## ✅ Features

* `Customer` with name validation (1–15 characters)
* `Coffee` with immutable names (at least 3 characters)
* `Order` linking a customer and coffee with validated price (1.0–10.0)
* Relationships:

  * Customers can place multiple orders
  * Coffees track all orders and unique customers
* Aggregates:

  * Number of orders per coffee
  * Average price for a coffee
* **Bonus**: Identify the customer who spent the most on a specific coffee

---

## 🧪 Running the Tests

To run all tests:

```bash
PYTHONPATH=. pytest
```

You should see output like:

```
11 passed in 0.13s
```

---

## 🐞 Debug Mode

To view sample orders, coffee stats, and relationship outputs:

```bash
PYTHONPATH=. python debug.py
```

Expected sample output:

```
🧞 Orders for Alice:
  Latte - $4.5
  Mocha - $5.0

☕ Coffees ordered by Charlie: ['Espresso', 'Mocha', 'Latte']

📋 Orders for Latte:
  Alice - $4.5
  Bob - $6.0
  Charlie - $3.5

👥 Customers who ordered Mocha: ['Alice', 'Charlie']

📊 Latte orders count: 3
💰 Latte average price: $4.67

🏆 Most aficionado of Latte: Bob
```

---

## 📌 Requirements

* Python 3.8+
* `pytest` installed:

  ```bash
  pip install pytest
  ```

---

## 📬 Author

Made with ❤️ by \[MUCHIRI DENNIS]
