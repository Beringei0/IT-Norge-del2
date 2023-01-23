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
    c.execute('''CREATE TABLE IF NOT EXISTS kundeinfo (
    kundenr  INTEGER PRIMARY KEY,
    fnavn    TEXT,
    enavn    TEXT,
    epost    TEXT,
    tlf      INTEGER,
    postnr   INTEGER
    )''')
    
    # creates table "postnummer_tabell"
    c.execute('''CREATE TABLE IF NOT EXISTS postnummer_tabell(
    postnummer  INTEGER,
    poststed    TEXT,
    kommunenr   INTEGER,
    kommunenavn TEXT,
    kategori    TEXT   
    )''')

def joinColumns():
    c.execute('''SELECT postnr
     FROM kundeinfo
     INNER JOIN postnummer_tabell
     ON postnummer_tabell.postnummer = kundeinfo.postnr
     ''')
    conn.commit()

def insrtKundeinfo():
    with open ('randoms.csv', 'r') as f:
        dr = csv.DictReader(f)
        to_kundeinfo = [(i['fname'], i['ename'], i['epost'], i['tlf'])for i in dr]
        c.executemany('INSERT INTO kundeinfo (fnavn, enavn, epost, tlf) VALUES (?, ?, ?, ?)', to_kundeinfo)
        conn.commit()

def insrtPostnr():
    with open ('Postnummerregister.csv', 'r') as f:
        dr = csv.DictReader(f)
        to_postnummer = [(i['Postnummer'], i['Poststed'], i['Kommunenummer'], i['Kommunenavn'], i['Kategori'])for i in dr]
        c.executemany('INSERT INTO postnummer_tabell (postnummer, poststed, kommunenr, kommunenavn, kategori) VALUES (?, ?, ?, ?, ?)', to_postnummer)
        conn.commit()

def inputField():
    type = str(input("Would like to close this DB y/n?: "))

    if type == "y":
        print("DB has been closed")
        conn.close()
    elif type == "n":
        print("Changes will be made to DB")
        


    
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
    printRows()

    
