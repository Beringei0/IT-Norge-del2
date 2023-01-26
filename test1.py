import sqlite3 as sq
import csv
#-------------------every imported module 

# main functions 
def main():
    global conn# makes var "conn" global 
    global c# make var "cursor" global

    conn = sq.connect('kundeliste.db')# creates a new table "kundeliste.db"
    c = conn.cursor()# creates a cursor for DB 
    c.execute('PRAGMA foreign_keys = ON;')
    creatTables()
    insrtPostnr()
    insrtKundeinfo()
    commit()
    printRows()


# function that creates tables for "kundeliste" DB
def creatTables():
    # creates table "postnummer_tabell"
    c.execute('''CREATE TABLE IF NOT EXISTS postnummer_tabell(
      postnummer  INTEGER PRIMARY KEY, 
      poststed    TEXT    NOT NULL,
      kommunenr   INTEGER NOT NULL,
      kommunenavn TEXT    NOT NULL,
      kategori    TEXT    NOT NULL
    )''')

    # creates table "Kundeliste"
    c.execute('''CREATE TABLE IF NOT EXISTS kundeinfo(
       kundenr  TEXT PRIMARY KEY NOT NULL,
       fnavn    TEXT NOT NULL,
       enavn    TEXT NOT NULL,
       epost    TEXT NOT NULL,
       tlf      INTEGER NOT NULL,
       postnummer   INTEGER NOT NULL,
       FOREIGN KEY (postnummer) REFERENCES postnummer(postnummer_tabell)
    )''')


def insrtKundeinfo():
    with open ('randoms.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            c.execute('INSERT INTO kundeinfo (fnavn, enavn, epost, tlf, postnummer) VALUES (?, ?, ?, ?, ?)', row)

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


def commit():
    conn.commit()  

def printRows():
        for row in c.execute('SELECT * FROM kundeinfo'):
            print(row)


# if main block 
if __name__=='__main__':
    main()
   
    
