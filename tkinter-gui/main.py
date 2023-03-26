import sqlite3 as sq
import tkinter as tk
#-------------------every imported module

# initializes the tkinter window
root = tk.Tk()
# positions window at center 
root.eval("tk::PlaceWindow . center")

# main function holding all functions 
def main():
    labels()
    entries()
    buttons()
    search()
    insrt_data() 
    mainloop()

# function that includes every tk button 
def buttons():
    global result_listbox
    global search_button

    search_button = tk.Button(root, text="search")
    search_button.grid(row=2, column=0)

    result_listbox = tk.Listbox(root, height=1, width=70)
    result_listbox.grid(row=3, column=0, pady=10)

    add_data_button = tk.Button(root, text="add data", command=insrt_data)
    add_data_button.grid(row=14, column=0) 

    delete_button = tk.Button(root, text='delete', command=del_row)
    delete_button.grid(row=19, column=0)


# function that includes every tk entry fields
def entries():
    global name_entry
    global search_entry
    global suname_entry
    global delete_entry
    global email_entry

    search_entry = tk.Entry(root, width=30)
    search_entry.grid(row=1, column=0)

    name_entry = tk.Entry(root, width=30)
    name_entry.grid(row=8, column=0)

    suname_entry = tk.Entry(root, width=30)
    suname_entry.grid(row=11, column=0)

    email_entry = tk.Entry(root, width=30)
    email_entry.grid(row=13, column=0)  

    delete_entry = tk.Entry(root, width=30)
    delete_entry.grid(row=17, column=0)  
    
# function that includes every tk label 
def labels():
    search_label = tk.Label(root, text='søk etter kunder')
    search_label.grid(row=0, column=0)

    add_data_label = tk.Label(root, text='legg inn nye kunder')
    add_data_label.grid(row=4, column=0)

    name_label = tk.Label(root, text="Name")
    name_label.grid(row=7, column=0)

    suname_label = tk.Label(root, text="Surname")
    suname_label.grid(row=10, column=0)

    email_label = tk.Label(root, text="Email")
    email_label.grid(row=12, column=0)

    delete_label = tk.Label(root, text="slett kunde via kundenummer(sletter fra test.db)")
    delete_label.grid(row=16, column=0, pady=5)

# search function that finds db objects based on the search_entry
def search():
    # creates connection to DB
    conn = sq.connect('tkinter-gui/kundeliste.db')
    cur = conn.cursor()

    query = search_entry.get()
    # selects kundenr based on the "kundenr" entered in the "search_entry" variable
    cur.execute("SELECT * FROM kundeinfo WHERE kundenr LIKE ?", ('%' + query + '%',))
    data = cur.fetchall()
    result_listbox.delete(0, tk.END)

    for row in data:
        result_listbox.insert(tk.END, row)
        
    search_button.configure(command=search)

# function that insert data from the tk entries
def insrt_data():
    # creates connection to test.db
    conn = sq.connect('tkinter-gui/test.db')
    cur = conn.cursor()

    name = name_entry.get()
    suname = suname_entry.get()
    email = email_entry.get()

    # inserts values of the "name", "suname" and "email" variables into "Name" table 
    cur.execute('INSERT INTO Name (fname, age, email) VALUES (?, ?, ?)', (name, suname, email))

    name_entry.delete(0, tk.END)
    suname_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    conn.commit()

# function that delete rows based on delete entry
def del_row():
    query = delete_entry.get()
    conn = sq.connect('tkinter-gui/test.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Name WHERE kundenr LIKE ?", ('%' + query + '%',))
    conn.commit()

    delete_entry.delete(0, tk.END)

# initializes all tkinter objects and widgets
def mainloop():
    root.mainloop()


if __name__=='__main__':
    main()





    





