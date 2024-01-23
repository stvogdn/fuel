from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Database operations (similar to previous implementation)
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

# API to insert data
@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    date = data['date']
    odometer = data['odometer']
    gallons = data['gallons']
    price_per_gallon = data['price_per_gallon']
    total_cost = data['total_cost']

    # Calculations
    last_odometer = get_last_odometer()
    distance = odometer - last_odometer if last_odometer is not None else 0
    mileage = distance / gallons if gallons > 0 else 0

    # Insert into DB
    insert_data(date, odometer, gallons, price_per_gallon, total_cost, distance, mileage)

    return jsonify({
        'message': 'Data entered successfully',
        'distance': distance,
        'mileage': mileage
    })

if __name__ == '__main__':
    app.run(debug=True)
