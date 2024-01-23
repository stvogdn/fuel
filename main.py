import sqlite3

def insert_data(date, odometer, gallons, price_per_gallon, total_cost, distance, mileage):
    conn = sqlite3.connect('gas_mileage.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO mileage_data (date, odometer, gallons, price_per_gallon, total_cost, distance, mileage)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (date, odometer, gallons, price_per_gallon, total_cost, distance, mileage))
    conn.commit()
    conn.close()

def get_last_odometer():
    conn = sqlite3.connect('gas_mileage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT odometer FROM mileage_data ORDER BY id DESC LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def main():
    # Accept inputs
    date = input("Enter the date (YYYY-MM-DD): ")
    odometer = float(input("Enter the odometer reading (miles): "))
    gallons = float(input("Enter the gallons filled: "))
    price_per_gallon = float(input("Enter the price per gallon: "))
    total_cost = float(input("Enter the total cost: "))

    # Calculate distance traveled since the last entry and mileage
    last_odometer = get_last_odometer()
    distance = odometer - last_odometer if last_odometer is not None else 0
    mileage = distance / gallons if gallons > 0 else 0

    # Insert data into the database
    insert_data(date, odometer, gallons, price_per_gallon, total_cost, distance, mileage)

    print("Data entered successfully.")
    if last_odometer is not None:
        print(f"Distance traveled since last entry: {distance} miles")
        print(f"Mileage: {mileage} miles per gallon")

if __name__ == "__main__":
    main()
