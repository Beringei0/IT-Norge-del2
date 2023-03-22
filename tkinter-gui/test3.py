import sqlite3 as sq
import tkinter as tk
#-------------------every imported module

global cur

# if main function
def main(): 
    conn()
    root()

# function that connects to existing database
def conn():
    conn = sq.connect('tkinter-gui/kundeliste.db')
    cur = conn.cursor()

# initalizes 
def root():
    global search_entry 
    root = tk.Tk()
    root.eval("tk::PlaceWindow . center")

    search_label = tk.Label(root, text='søk etter kunder').grid(row=0, column=0)
    search_entry = tk.Entry(root).grid(row=0, column=1)   


    root.mainloop()

def search():
    query = search_entry

    cur







    





if __name__=='__main__':
    main()
