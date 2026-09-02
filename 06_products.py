products = {
    "Laptop": 55000,
    "Phone": 30000,
    "Headphones": 2000,
    "Mouse": 700,
    "Keyboard": 1500
}

for product, price in products.items():

    if price > 2000:
        print(product, "-> ₹", price)