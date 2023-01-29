import sqlite3 as sq
import csv
#-------------------every imported module 

# main function calls every function
def main():
    createDB()
    creatTables()
    insrtPostnr()
    insrtKundeinfo()
    delete()
    printRows()
    commit()
    searchInfo()

# creates the database 
def createDB():
    global conn# makes var "conn" global 
    global c# make var "cursor" global

    conn = sq.connect('kundeliste.db')# creates a new table "kundeliste.db"
    c = conn.cursor()# creates a cursor for DB 
    c.execute('PRAGMA foreign_keys = 0;')


# function that creates tables for "kundeliste" DB
def creatTables():

    # creates table "postnummer_tabell"
    c.execute('''CREATE TABLE IF NOT EXISTS postnummer_tabell(
    postnummer  INTEGER PRIMARY KEY NOT NULL,
    poststed    TEXT NOT NULL,
    kommunenr   INTEGER NOT NULL,
    kommunenavn TEXT NOT NULL,
    kategori    TEXT NOT NULL  
    )''')
 
    # creates table "Kundeliste"
    c.execute('''CREATE TABLE IF NOT EXISTS kundeinfo (
    kundenr  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    fnavn    TEXT NOT NULL,
    enavn    TEXT NOT NULL,
    epost    TEXT NOT NULL,
    tlf      INTEGER,
    postnr   INTEGER NOT NULL, 
    FOREIGN KEY (postnr) REFERENCES postnummer_tabell (postnummer)
    )''')


# function that reads "Postnummerregister.csv" as dict and inserts key values to kundeinfo table
def insrtPostnr():
    with open ('Postnummerregister.csv', 'r') as f:
        dr = csv.DictReader(f)# reads csv file as dict
        to_postnummer = [(i['Postnummer'], i['Poststed'], i['Kommunenummer'], i['Kommunenavn'], i['Kategori'])for i in dr]# keys
        c.executemany('INSERT INTO postnummer_tabell (postnummer, poststed, kommunenr, kommunenavn, kategori) VALUES (?, ?, ?, ?, ?)', to_postnummer)# gives keys values 


# function that reads "randoms.csv" as dict and inserts key values to kundeinfo table
def insrtKundeinfo():
    with open ('randoms.csv', 'r') as f:
        dr = csv.DictReader(f)# reads csv file as dict
        to_kundeinfo = [(i['fname'], i['ename'], i['epost'], i['tlf'], i['postnummer'])for i in dr]# keys
        c.executemany('INSERT INTO kundeinfo (fnavn, enavn, epost, tlf, postnr) VALUES (?, ?, ?, ?, ?)', to_kundeinfo)# gives keys values 


# function that allows you to search for costumers via "kundenr"
def searchInfo():
    # input field 
    search = input("søk etter kunde: ")

    # list with both table columns
    list = ("kundenr", "fnavn", "enavn", "epost", "tlf", "postnr", "poststed", "kommunenr", "kommunenavn", "kategori")

    # inner joins table "kuneinfo.postnr", "postnummer_tabell.postnummer" and finds value specified in "search"
    results = c.execute('''SELECT 
    kundeinfo.kundenr,
    kundeinfo.fnavn,
    kundeinfo.enavn, 
    kundeinfo.epost, 
    kundeinfo.tlf,
    kundeinfo.postnr,
    postnummer_tabell.poststed,
    postnummer_tabell.kommunenr,
    postnummer_tabell.kommunenavn,
    postnummer_tabell.kategori
    FROM kundeinfo
    INNER JOIN postnummer_tabell
    ON kundeinfo.[postnr] = postnummer_tabell.[postnummer]
    WHERE kundeinfo.kundenr = ?''',(search,))

    # for loop prints "results" and "list"
    for results in results:
        print(list)
        print(results)
        

# fucntion that print every row in "kundeinfo" table with for loop
def printRows():
    query = '''SELECT 
    kundeinfo.kundenr,
    kundeinfo.fnavn,
    kundeinfo.enavn, 
    kundeinfo.epost, 
    kundeinfo.tlf,
    kundeinfo.postnr,
    postnummer_tabell.poststed,
    postnummer_tabell.kommunenr,
    postnummer_tabell.kommunenavn,
    postnummer_tabell.kategori
    FROM kundeinfo
    INNER JOIN postnummer_tabell
    ON kundeinfo.postnr = postnummer_tabell.postnummer
    '''
    c.execute(query)
    results = c.fetchall()

    for results in results:
        print(results)


# function that deletes the first row from "kundeinfo" table
def delete():
    c.execute('DELETE FROM kundeinfo WHERE kundenr = 1')

# fucntion that commits changes made to "kundeliste.db"
def commit():
    conn.commit()  

# if main line
if __name__=='__main__':
    main()

    
