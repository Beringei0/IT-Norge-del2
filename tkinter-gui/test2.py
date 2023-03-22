import tkinter as tk
import sqlite3

# Connect to the database
conn = sqlite3.connect('tkinter-gui/kundeliste.db')
c = conn.cursor()

# Define a function to search for data in the database
def search():
    # Get the search query from the text box
    query = search_box.get()
    # Execute a SELECT statement to search for the query in the database
    c.execute("SELECT * FROM kundeinfo WHERE kundenr LIKE ?", ('%' + query + '%',))
    data = c.fetchall()
    # Clear the listbox
    listbox.delete(0, tk.END)
    # Insert the search results into the listbox
    for row in data:
        listbox.insert(tk.END, row)

# Create a Tkinter window
window = tk.Tk()

frame1 = tk.Frame(window, width=500, height=500)
frame1.grid(row=0, column=0)

# Create a text box for the search query
search_box = tk.Entry(window)
search_box.pack()

# Create a button to execute the search
search_button = tk.Button(window, text="Search", command=search)
search_button.pack()

# Create a listbox to display the search results
listbox = tk.Listbox(window)
listbox.pack()

# Start the Tkinter event loop
window.mainloop()

# Close the database connection
conn.close()