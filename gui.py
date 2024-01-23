import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to insert data into the database
def insert_data(date, odometer, gallons, price_per_gallon, total_cost, distance, mileage):
    conn = sqlite3.connect('gas_mileage.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO mileage_data (date, odometer, gallons, price_per_gallon, total_cost, distance, mileage)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (date, odometer, gallons, price_per_gallon, total_cost, distance, mileage))
    conn.commit()
    conn.close()

# Function to get the last odometer reading from the database
def get_last_odometer():
    conn = sqlite3.connect('gas_mileage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT odometer FROM mileage_data ORDER BY id DESC LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Function to submit data from the form
def submit_data():
    # Get values from input fields
    date = date_entry.get()
    odometer = float(odometer_entry.get())
    gallons = float(gallons_entry.get())
    price_per_gallon = float(price_per_gallon_entry.get())
    total_cost = float(total_cost_entry.get())

    # Calculate distance and mileage
    last_odometer = get_last_odometer()
    distance = odometer - last_odometer if last_odometer is not None else 0
    mileage = distance / gallons if gallons > 0 else 0

    # Insert data into the database
    insert_data(date, odometer, gallons, price_per_gallon, total_cost, distance, mileage)

    # Display success message
    messagebox.showinfo("Success", "Data entered successfully.")
    if last_odometer is not None:
        messagebox.showinfo("Results", f"Distance traveled since last entry: {distance} miles\nMileage: {mileage} miles per gallon")

    # Clear input fields
    date_entry.delete(0, tk.END)
    odometer_entry.delete(0, tk.END)
    gallons_entry.delete(0, tk.END)
    price_per_gallon_entry.delete(0, tk.END)
    total_cost_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Gas Mileage Tracker")

# Create and place input fields and labels
tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1)

tk.Label(root, text="Odometer Reading (miles):").grid(row=1, column=0)
odometer_entry = tk.Entry(root)
odometer_entry.grid(row=1, column=1)

tk.Label(root, text="Gallons Filled:").grid(row=2, column=0)
gallons_entry = tk.Entry(root)
gallons_entry.grid(row=2, column=1)

tk.Label(root, text="Price per Gallon:").grid(row=3, column=0)
price_per_gallon_entry = tk.Entry(root)
price_per_gallon_entry.grid(row=3, column=1)

tk.Label(root, text="Total Cost:").grid(row=4, column=0)
total_cost_entry = tk.Entry(root)
total_cost_entry.grid(row=4, column=1)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit Data", command=submit_data)
submit_button.grid(row=5, column=0, columnspan=2)

# Start the main loop
root.mainloop()
