import tkinter as tk
import sqlite3 as sq
#------------------every imported module 


def main():
    DBconn()

# function that connects to the "kundeliste" database
def DBconn():
    conn = sq.connect('tkinter-gui/kundeliste.db')
    cur = conn.cursor

def root():
    root = tk.Tk()







if __name__ =='__main__':
    main()
