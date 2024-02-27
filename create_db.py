"""create sqlite db"""
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('gas_mileage.db')
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''
CREATE TABLE IF NOT EXISTS "mileage_data" (
	"id"	INTEGER,
	"date"	TEXT NOT NULL,
	"odometer"	INTEGER NOT NULL,
	"gallons"	REAL NOT NULL,
	"price_per_gallon"	NUMERIC NOT NULL,
	"total_cost"	NUMERIC NOT NULL,
	"location"	TEXT,
	"distance"	INTEGER,
	"mileage"	INTEGER,
	PRIMARY KEY("id")
)
''')

conn.commit()
conn.close()
