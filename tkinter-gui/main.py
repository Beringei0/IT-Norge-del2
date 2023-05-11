import sqlite3 as sq
import tkinter as tk
import webbrowser as web 
import hashlib
#-------------------every imported module

# main function holding all functions 
def main():
    window_main()
    login()
    labels_main()
    entries_main()
    buttons_main()
    search()
    insrt_data() 
    mainloop()

# function for the main window
def window_main():
    global main_window
    # initializes the tkinter window
    main_window = tk.Tk()
    # positions window at center 
    main_window.eval("tk::PlaceWindow . center")
    # using the withdraw method to hide window
    main_window.withdraw()

# function that includes every tk button in the "main_window" function 
def buttons_main():
    global result_listbox
    global search_button

    search_button = tk.Button(main_window, text="search")# 
    search_button.grid(row=2, column=1)

    result_listbox = tk.Listbox(main_window, height=1, width=70)
    result_listbox.grid(row=3, column=1, pady=10, padx=40)

    add_data_button = tk.Button(main_window, text="add data", command=insrt_data)
    add_data_button.grid(row=14, column=1) 

    delete_button = tk.Button(main_window, text='delete', command=del_row)
    delete_button.grid(row=19, column=1)

    faq_button = tk.Button(main_window, text="FAQ", command=faq)
    faq_button.grid(row=0, column=0, ipadx=7)

    back_button = tk.Button(main_window, text="Tilbake", command=lambda:[main_window.withdraw(), login_window.deiconify()])
    back_button.grid(row=1, column=0, pady=5)

# function that includes every tk entry fields in the "main_window" function 
def entries_main():
    global name_entry
    global search_entry
    global suname_entry
    global delete_entry
    global email_entry

    search_entry = tk.Entry(main_window, width=30)
    search_entry.grid(row=1, column=1)

    name_entry = tk.Entry(main_window, width=30)
    name_entry.grid(row=8, column=1)

    suname_entry = tk.Entry(main_window, width=30)
    suname_entry.grid(row=11, column=1)

    email_entry = tk.Entry(main_window, width=30)
    email_entry.grid(row=13, column=1)  

    delete_entry = tk.Entry(main_window, width=30)
    delete_entry.grid(row=17, column=1)  
    
# function that includes every tk label in the "main_window" function 
def labels_main():
    #Tkinter label objects 
    search_label = tk.Label(main_window, text='søk etter kunder')
    search_label.grid(row=0, column=1)

    add_data_label = tk.Label(main_window, text='legg inn nye kunder')
    add_data_label.grid(row=4, column=1)

    name_label = tk.Label(main_window, text="Name")
    name_label.grid(row=7, column=1)

    suname_label = tk.Label(main_window, text="Surname")
    suname_label.grid(row=10, column=1)

    email_label = tk.Label(main_window, text="Email")
    email_label.grid(row=12, column=1)

    delete_label = tk.Label(main_window, text="slett kunde via kundenummer(sletter fra test.db)")
    delete_label.grid(row=16, column=1, pady=5)

# Login function that appears when launching the code 
def login():
    global uname_entry_login
    global passw_entry_login
    global login_status
    global login_window

    login_window = tk.Tk()# Tkinter window for the login screen 
    login_window.eval("tk::PlaceWindow . center")# positions window at center 

    uname_label = tk.Label(login_window, text="Username")# label for username widget 
    uname_label.grid(pady=3, padx=20)

    uname_entry_login = tk.Entry(login_window, width=20)# entry field for username
    uname_entry_login.grid(pady=5, padx=20)

    passw_label = tk.Label(login_window, text="Password")# label for password
    passw_label.grid(pady=5, padx=20)

    passw_entry_login = tk.Entry(login_window, width=20, show="*")# entry feild for password
    passw_entry_login.grid(pady=5, padx=20)

    login_button = tk.Button(login_window, text="Login", command=check_login)# button for login option 
    login_button.grid(pady=5, padx=20)

    register_label = tk.Label(login_window, text="(Har ikke en bruker?)")# label for registration button
    register_label.grid(pady=1, padx=20)

    register_button = tk.Button(login_window, text="Registrer", command=register )# button for registration of a account 
    register_button.grid(pady=1, padx=20)

    login_status = tk.Label(login_window, text="")
    login_status.grid(pady=5, padx=20)

# function for the registration of new accounts
def register():
    global uname_register_entry
    global passw_register_entry
    global register_window

    # hides the long window when making new account in the "Register" screen
    login_window.withdraw()

    register_window = tk.Tk()# creates new Tkinter window
    register_window.eval("tk::PlaceWindow . center")# places window at center

    register_label = tk.Label(register_window,text="Skriv inn ønsket brukernavn og passord")# label for register window
    register_label.grid(pady=5, padx=20)

    uname_label = tk.Label(register_window, text="Brukernavn")# label for username widget 
    uname_label.grid(pady=3, padx=20)

    uname_register_entry = tk.Entry(register_window, width=20)# entry field for username
    uname_register_entry.grid(pady=5, padx=20)

    passw_label = tk.Label(register_window, text="Passord")# label for password
    passw_label.grid(pady=5, padx=20)

    passw_register_entry = tk.Entry(register_window, width=20, show="*")# entry feild for password
    passw_register_entry.grid(pady=5, padx=20)

    register_button = tk.Button(register_window, text="Registrer", command=hash_passw)# button for login option 
    register_button.grid(pady=5, padx=20)  

    # button using a lambda function to store multiple arguements 
    back_button = tk.Button(register_window, text="Tilbake", command=lambda:[register_window.withdraw(), login_window.deiconify()])
    back_button.grid(row=6, column=0)

# function that checks for correct login input 
def check_login():
    # gets entries from the variables
    password = passw_entry_login.get()
    username = uname_entry_login.get()

    # uses hashlib to encrypt password with hexadecimals 
    hashed_passw = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # create a connection to the users database
    conn = sq.connect('tkinter-gui/kundeliste.db')
    cur = conn.cursor()

    # selects values from "username" and "password" input based on where it is in the users database
    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    result = cur.fetchone()
    
    # if not none statement that responds if the "result" variable has a none value 
    if result is not None: 
        if hashed_passw == result[1]:# if statement that checks if the encrypted password matches the result tuple of 1
            main_window.deiconify()
            login_window.withdraw()
        else:
            login_status.config(text="(Feil brukernavn eller passord)")
    else:
        login_status.config(text="(Feil brukernavn eller passord)")

    passw_entry_login.delete(0, tk.END)
    uname_entry_login.delete(0, tk.END)

# function that inserts new accounts
def insertuser():
    # creates connection to test.db
    conn = sq.connect('tkinter-gui/kundeliste.db')
    cur = conn.cursor()

    # gets input from the "register" function
    username = uname_register_entry.get() 

    # inserts values of the "uname" and "passw" variables into "user_info" table 
    cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_passw))

    # resets input fields
    uname_register_entry.delete(0, tk.END)
    passw_register_entry.delete(0, tk.END)

    # commits changes to the database
    conn.commit()

# function that encrypts password
def hash_passw():
    global hashed_passw
    
    # gets input from variable 
    password = passw_register_entry.get()# gets input from variable 
    
    # takes input and hashes the password input 
    hashed_passw = hashlib.sha256(password.encode('utf-8')).hexdigest()

    insertuser()

    print(hashed_passw)

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
    # gets entry for "delete_entry" variable 
    query = delete_entry.get()

    conn = sq.connect('tkinter-gui/test.db')# creates connection with the "test" database
    cur = conn.cursor()# created a cursor for editing the "test" database

    # deletes info based on what value the "query" variable holds
    cur.execute("DELETE FROM Name WHERE kundenr LIKE ?", ('%' + query + '%',))
    conn.commit()

    delete_entry.delete(0, tk.END)

# function that stores every widget included in the FAQ window
def faq():
    global faq_window

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

# function that redirects to the link below when "question_button" above is called
def redirect():
    web.open("https://askodegaard.on.spiceworks.com/portal")

# initializes all tkinter objects and widgets
def mainloop():
    main_window.mainloop()


if __name__=='__main__':
    main()





    





