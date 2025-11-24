# 1. Dictionary with 5 products
inventory = {
    "Laptop": 15,
    "Headphones": 8,
    "Mouse": 25,
    "Keyboard": 12,
    "USB Cable": 5
}

print("Initial Inventory:", inventory)

# 2. Add & Update product
inventory["Smartphone"] = 20
inventory["Mouse"] = 30
print("\nAfter Add & Update:", inventory)

# 3. Function to return products with stock < 10
def low_stock(inv):
    return {key: val for key, val in inv.items() if val < 10}

print("\nLow Stock Products (<10):", low_stock(inventory))

# 4. Delete discontinued product
del inventory["USB Cable"]
print("\nAfter Deleting 'USB Cable':", inventory)

# 5. Loop through items
print("\nAll Products & Quantities:")
for product, qty in inventory.items():
    print(product, ":", qty)
