import tkinter as tk
import sqlite3

# Create a Tkinter window
window = tk.Tk()
window.title("Add Data")

# Create a Frame widget within the window
frame = tk.Frame(window)
frame.pack(padx=10, pady=10)

# Create Labels and Entry widgets for the input fields
name_label = tk.Label(frame, text="Name:")
name_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

age_label = tk.Label(frame, text="Age:")
age_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
age_entry = tk.Entry(frame)
age_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = tk.Label(frame, text="Email:")
email_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(frame)
email_entry.grid(row=2, column=1, padx=5, pady=5)

# Create a function to insert data into the database
def insert_data():
    # Retrieve the data from the Entry widgets
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()

    # Connect to the database
    conn = sqlite3.connect('tkinter-gui/test.db')
    c = conn.cursor()

    # Execute the INSERT query to add the data to the database
    c.execute("INSERT INTO Name (fname, age, email) VALUES (?, ?, ?)", (name, age, email))

    # Commit the changes to the database and close the connection
    conn.commit()
    conn.close()

    # Clear the Entry widgets
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Create a Button widget to trigger the insertion of data
insert_button = tk.Button(frame, text="Add Data", command=insert_data)
insert_button.grid(row=3, column=1, padx=5, pady=5)

# Run the Tkinter event loop
window.mainloop()
