import sqlite3 as sq
import tkinter as tk
import webbrowser as web 
#-------------------every imported module

def window():
    global main_window
    # initializes the tkinter window
    main_window = tk.Tk()
    # positions window at center 
    main_window.eval("tk::PlaceWindow . center")


# main function holding all functions 
def main():
    window()
    login()
    labels()
    entries()
    buttons()
    search()
    insrt_data() 
    mainloop()

# Login function that appears when launching the code 
def login():
    # Tkinter window for the login screen 
    login_window = tk.Tk()
    # positions window at center 
    login_window.eval("tk::PlaceWindow . center")


    


# function that includes every tk button 
def buttons():
    global result_listbox
    global search_button

    search_button = tk.Button(main_window, text="search")
    search_button.grid(row=2, column=0)

    result_listbox = tk.Listbox(main_window, height=1, width=70)
    result_listbox.grid(row=3, column=0, pady=10)

    add_data_button = tk.Button(main_window, text="add data", command=insrt_data)
    add_data_button.grid(row=14, column=0) 

    delete_button = tk.Button(main_window, text='delete', command=del_row)
    delete_button.grid(row=19, column=0)

    faq_button = tk.Button(main_window, text="FAQ", command=faq_window)
    faq_button.grid(row=0, column=1)


# function that includes every tk entry fields
def entries():
    global name_entry
    global search_entry
    global suname_entry
    global delete_entry
    global email_entry

    #Tkinter eentry fields 
    search_entry = tk.Entry(main_window, width=30)
    search_entry.grid(row=1, column=0)

    name_entry = tk.Entry(main_window, width=30)
    name_entry.grid(row=8, column=0)

    suname_entry = tk.Entry(main_window, width=30)
    suname_entry.grid(row=11, column=0)

    email_entry = tk.Entry(main_window, width=30)
    email_entry.grid(row=13, column=0)  

    delete_entry = tk.Entry(main_window, width=30)
    delete_entry.grid(row=17, column=0)  
    
# function that includes every tk label 
def labels():

    #Tkinter label objects 
    search_label = tk.Label(main_window, text='søk etter kunder')
    search_label.grid(row=0, column=0)

    add_data_label = tk.Label(main_window, text='legg inn nye kunder')
    add_data_label.grid(row=4, column=0)

    name_label = tk.Label(main_window, text="Name")
    name_label.grid(row=7, column=0)

    suname_label = tk.Label(main_window, text="Surname")
    suname_label.grid(row=10, column=0)

    email_label = tk.Label(main_window, text="Email")
    email_label.grid(row=12, column=0)

    delete_label = tk.Label(main_window, text="slett kunde via kundenummer(sletter fra test.db)")
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

# function that stores every widget included in the FAQ window
def faq_window():
    faq_window = tk.Tk()

    faq_text = tk.Label(faq_window, text="""
    FAQ:
    Hvordan oppretter jeg en ny bruker i Spiceworks Cloud Help Desk?:

    * Logg inn på administratorkonsollen og gå til "Settings" (Innstillinger).
    * Under "User Management" (Brukerhåndtering), velg "New User" (Ny bruker).
    * Fyll ut nødvendig informasjon om brukeren og klikk på "Save" (Lagre) for å opprette den nye brukeren.

    Hvordan oppretter jeg en ny sak i Spiceworks Cloud Help Desk?:

    * Logg inn på brukerportalen eller administratorkonsollen.
    * Klikk på "New Ticket" (Ny sak) eller "Submit a Request" (Send en henvendelse).
    * Fyll ut informasjonen om saken, inkludert tittel, beskrivelse og eventuelle vedlegg.
    * Klikk på "Submit" (Send) for å opprette den nye saken.

    Hvordan tildeles en sak til en bestemt tekniker i Spiceworks Cloud Help Desk?:

    * Åpne den aktuelle saken i administratorkonsollen.
    * Finn delen "Assigned To" (Tildelt til) og velg den ønskede teknikeren fra rullegardinmenyen.
    * Klikk på "Save" (Lagre) for å oppdatere saken med den nye tildelingen.""")
    faq_text.grid(row=0, column=0)

    question_button = tk.Button(faq_window, text="send spørsmål", command=redirect)
    question_button.grid(padx=5, pady=5)

def redirect():
    web.open("https://askodegaard.on.spiceworks.com/portal")


# initializes all tkinter objects and widgets
def mainloop():
    main_window.mainloop()


if __name__=='__main__':
    main()





    





