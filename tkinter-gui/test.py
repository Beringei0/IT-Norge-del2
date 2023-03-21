import tkinter as tk

def validate_login(username, password):
    # Check the username and password against a database or hardcoded values
    if username == "example" and password == "password":
        return True
    else:
        return False

def on_submit():
    username = username_entry.get()
    password = password_entry.get()
    if validate_login(username, password):
        result_label.config(text="Login successful!")
    else:
        result_label.config(text="Incorrect username or password")

# Create the login form window
window = tk.Tk()
window.title("Login Form")

# Add labels and entry boxes for username and password
tk.Label(window, text="Username").grid(row=0, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)

tk.Label(window, text="Password").grid(row=1, column=0)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1)

# Add a submit button that calls the validation function
submit_button = tk.Button(window, text="Submit", command=on_submit)
submit_button.grid(row=2, column=1)

# Add a label to display the validation result
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=1)

# Run the window loop
window.mainloop()
