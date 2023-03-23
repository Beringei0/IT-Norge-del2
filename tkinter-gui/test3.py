import sqlite3 as sq
import tkinter as tk
#-------------------every imported module


root = tk.Tk()
root.eval("tk::PlaceWindow . center")

def window():
    global search_entry
    global result_listbox
    global search_button
    global name_entry
    global suname_entry
    global email_entry
    global delete_entry

    search_label = tk.Label(root, text='søk etter kunder')
    search_label.grid(row=0, column=0)

    search_entry = tk.Entry(root, width=30)
    search_entry.grid(row=1, column=0)

    search_button = tk.Button(root, text="search")
    search_button.grid(row=2, column=0)

    result_listbox = tk.Listbox(root, height=1, width=70)
    result_listbox.grid(row=3, column=0, pady=10)

    add_data_label = tk.Label(root, text='legg inn nye kunder')
    add_data_label.grid(row=4, column=0)

    add_data_button = tk.Button(root, text="add data", command=insrt_data)
    add_data_button.grid(row=14, column=0)

    name_label = tk.Label(root, text="Name")
    name_label.grid(row=7, column=0)

    name_entry = tk.Entry(root, width=30)
    name_entry.grid(row=8, column=0)

    suname_label = tk.Label(root, text="Surname")
    suname_label.grid(row=10, column=0)

    suname_entry = tk.Entry(root, width=30)
    suname_entry.grid(row=11, column=0)

    email_label = tk.Label(root, text="Email")
    email_label.grid(row=12, column=0)

    email_entry = tk.Entry(root, width=30)
    email_entry.grid(row=13, column=0)    

    delete_button = tk.Button(root, text='delete', command=del_row)
    delete_button.grid(row=14, column=0)

    delete_entry = tk.Entry(root, width=30)
    delete_entry.grid(row=15, column=0)


def search():
    conn = sq.connect('tkinter-gui/kundeliste.db')
    cur = conn.cursor()

    query = search_entry.get()
    cur.execute("SELECT * FROM kundeinfo WHERE kundenr LIKE ?", ('%' + query + '%',))
    data = cur.fetchall()
    result_listbox.delete(0, tk.END)

    for row in data:
        result_listbox.insert(tk.END, row)
        
    
    search_button.configure(command=search)

    root.mainloop()



def insrt_data():
    conn = sq.connect('tkinter-gui/test.db')
    cur = conn.cursor()
    name = name_entry.get()
    suname = suname_entry.get()
    email = email_entry.get()

    cur.execute('INSERT INTO Name (fname, age, email) VALUES (?, ?, ?)', (name, suname, email))

    name_entry.delete(0, tk.END)
    suname_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    conn.commit()

def del_row():
    query = delete_entry.get()
    conn = sq.connect('tkinter-gui/test.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Name WHERE kundenr LIKE ?", ('%' + query + '%',))
    conn.commit()










window()
search()
insrt_data()




    





