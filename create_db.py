import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('gas_mileage.db')
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''
CREATE TABLE IF NOT EXISTS mileage_data (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    odometer REAL NOT NULL,
    gallons REAL NOT NULL,
    price_per_gallon REAL NOT NULL,
    total_cost REAL NOT NULL,
    distance REAL,
    mileage REAL
)
''')

conn.commit()
conn.close()
