import sqlite3 as sq
import csv
#-------------------every imported module 

# main functions 
def main():
    global conn# makes var "conn" global 
    global c# make var "cursor" global

    conn = sq.connect('kundeliste.db')# creates a new table "kundeliste.db"
    c = conn.cursor()# creates a cursor for DB 

# function that creates tables for "kundeliste" DB
def creatTables():
    # creates table "Kundeliste"
    
    # creates table "postnummer_tabell"
    c.execute('''CREATE TABLE IF NOT EXISTS postnummer_tabell(
    postnummer  INTEGER PRIMARY KEY NOT NULL,
    poststed    TEXT NOT NULL,
    kommunenr   INTEGER NOT NULL,
    kommunenavn TEXT NOT NULL,
    kategori    TEXT NOT NULL    
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS kundeinfo (
    kundenr  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    fnavn    TEXT NOT NULL,
    enavn    TEXT NOT NULL,
    epost    TEXT NOT NULL,
    tlf      INTEGER,
    postnr   INTEGER NOT NULL,
    FOREIGN KEY (postnr) REFERENCES postnummer_tabell (postnummer) 
    )''')
 
def insrtKundeinfo():
    with open ('randoms.csv', 'r') as f:
        dr = csv.DictReader(f)
        to_kundeinfo = [(i['fname'], i['ename'], i['epost'], i['tlf'], i['postnummer'])for i in dr]
        c.executemany('INSERT INTO kundeinfo (fnavn, enavn, epost, tlf, postnr) VALUES (?, ?, ?, ?, ?)', to_kundeinfo)

def insrtPostnr():
    with open ('Postnummerregister.csv', 'r') as f:
        dr = csv.DictReader(f)
        to_postnummer = [(i['Postnummer'], i['Poststed'], i['Kommunenummer'], i['Kommunenavn'], i['Kategori'])for i in dr]
        c.executemany('INSERT INTO postnummer_tabell (postnummer, poststed, kommunenr, kommunenavn, kategori) VALUES (?, ?, ?, ?, ?)', to_postnummer)

def inputField():
    type = str(input("Would like to close this DB y/n?: "))

    if type == "y":
        print("DB has been closed")
        conn.close()
    elif type == "n":
        print("Changes will be made to DB")


def menu():
    search = input("serach term: ")

    query = "SELECT * FROM kundeinfo WHERE kundenr LIKE'%{}%'".format(search)

    c.execute(query)
    results = c.execute('''SELECT * FROM kundeinfo WHERE kundeinfo.kundenr = ?''',(search))

    for results in results:
        print(results)


def joinColumns():
    query = '''SELECT 
    kundeinfo.kundenr,
    kundeinfo.fnavn,
    kundeinfo.enavn, 
    kundeinfo.epost, 
    kundeinfo.tlf,
    kundeinfo.postnr
    FROM kundeinfo
    INNER JOIN postnummer_tabell
    ON kundeinfo.postnr = postnummer_tabell.postnummer
    '''

    c.execute(query)
    results = c.fetchall()

    for results in results:
        print(results)


def commit():
    conn.commit()
        


    
def printRows():
    for row in c.execute('SELECT * FROM kundeinfo'):
        print(row)


# if main block 
if __name__=='__main__':
    main()
    creatTables()
    insrtKundeinfo()
    insrtPostnr()
    joinColumns()
    commit()
    #printRows()
    menu()

    
