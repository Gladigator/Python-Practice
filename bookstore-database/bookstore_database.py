# === Set Up the Database ===
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""
CREATE TABLE books (
    title TEXT,
    author TEXT,
    price REAL,
    sold INTEGER
)
""")

books = [
    ("The Hobbit", "Tolkien", 12.99, 150),
    ("Dune", "Herbert", 10.50, 200),
    ("1984", "Orwell", 9.99, 300),
    ("Sapiens", "Harari", 15.00, 120),
    ("Atomic Habits", "Clear", 13.50, 250)
]

cur.executemany(
    "INSERT INTO books VALUES (?, ?, ?, ?)",
    books
)

conn.commit()

print("Database ready with 5 books")

# === Total Copies Sold ===
cur.execute("SELECT SUM(sold) FROM books")

result = cur.fetchone()

total_sold = result[0]

print("Total books sold: " + str(total_sold))

# === Best Seller ===
cur.execute("SELECT title, sold FROM books ORDER BY sold DESC LIMIT 1")

result = cur.fetchone()

title = result[0]
sold = result[1]

print("Best seller: " + title + " (" + str(sold) + " sold)")

# === Average Price ===
cur.execute("SELECT AVG(price) FROM books")

result = cur.fetchone()

average = result[0]

print("Average price: $" + format(average, ".2f"))
