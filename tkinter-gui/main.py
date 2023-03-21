import tkinter as tk
import sqlite3 as sq
#------------------every imported module 


def main():
    DBconn()

# function that connects to the "kundeliste" database
def DBconn():
    conn = sq.connect('tkinter-gui/kundeliste.db')
    cur = conn.cursor

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

tk.Label(window, text="username").grid(row=0, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)

tk.Label(window, text="password").grid(row=1, column=0)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1)

submit_button = tk.Button(window, text="submit", command=sublogin)
submit_button.grid(row=2, column=1)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=1)

window.mainloop()

def tkinter():
    root = tk.Tk()
    root.title("Login")
    root.eval("tk::PlaceWindow . center")

    frame1 = tk.Frame(root, width=500, height=500)
    

    label_name = tk.Label(root, text="Name:")
    entry_name = tk.Entry(root)



    age_name = tk.Label(root, text="age:")
    entry_age = tk.Entry(root)

    button_submit = tk.Button(root, text="Submit")

    label_name.pack()
    entry_name()
    age_name()
    entry_age()
    button_submit()

    root.mainloop()

if __name__ =='__main__':
    main()
