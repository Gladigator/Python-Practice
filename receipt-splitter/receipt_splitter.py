# === Read the Receipt ===
items = []

with open("receipt.txt", "r") as file:
    for line in file:
        name, price = line.split()
        price = float(price)

        items.append((name, price))

print(f"Loaded {len(items)} items")

# === Total the Receipt ===
total = 0

for name, price in items:
    total = total + price

print(f"Total: ${total:.2f}")

# === Most Expensive Item ===
most_expensive_name = ""
most_expensive_price = 0

for name, price in items:
    if price > most_expensive_price:
        most_expensive_price = price
        most_expensive_name = name

print(f"Most expensive: {most_expensive_name} at ${most_expensive_price:.2f}")

# === Average Price ===
average = total / len(items)

print(f"Average price: ${average:.2f}")
