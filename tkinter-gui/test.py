import sqlite3 as sq
import tkinter as tk



def login(username, password):
    if username == "admin" and password =="admin":
        return True
    else:
        return False
    
def sublogin():
    username = username_entry.get()

    password = password_entry.get() 
    if login(username, password):
        result_label.config(text="login succesful!")
    else:
        result_label.config(text="incorrect username or password")


window = tk.Tk()
window.title('Login')
window.eval("tk::PlaceWindow . center")

tk.Label(window, text="username").grid(row=0, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)

window.mainloop()
