import sqlite3 as sq
import tkinter as tk
#-------------------every imported module

# main function holding all functions 
def main():
    create_db()
    test()

def create_db():
    # Create a connection object to the SQLite database
    conn = sq.connect('tkinter-gui/kundeliste.db')

    # Create a cursor object to interact with the database
    c = conn.cursor()

    # Create a table in the database
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')

    # Close the connection to the database
    conn.close()


def test():
    global uname_entry
    global passw_entry

    window = tk.Tk()
    window.eval("tk::PlaceWindow . center")

    uname_entry = tk.Entry(window, width=20)
    uname_entry.grid(row=0, column=0)

    passw_entry = tk.Entry(window,width=20)
    passw_entry.grid(row=1, column=0)

    insert_button = tk.Button(window, text="insert", command=insert)
    insert_button.grid(row=2, column=0)

    window.mainloop()

def insert():
    # creates connection to test.db
    conn = sq.connect('tkinter-gui/users.db')
    cur = conn.cursor()

    username = uname_entry.get()
    password = passw_entry.get()

    # inserts values of the "uname" and "passw" variables into "user_info" table 
    cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))


    conn.commit()
    




if __name__=='__main__':
    main()





    





