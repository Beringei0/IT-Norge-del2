import sqlite3 as sq
import pandas as pd 
#-------------------every imported module 


#------------main function
def main():
    global conn #makes the var "conn" global 
    global c #makes the var "c" global 

    conn = sq.connect('postnr.db') #creates a DB

    c = conn.cursor() #makes a cursor


#-------------------function that creates DB
def createtable():

    #creates a new table with column "kundenr" as primary
    table =('CREATE TABLE IF NOT EXISTS postnrtable (kundenr TEXT PRIMARY KEY, fname TEXT, ename TEXT, tlf INTEGER, postnummer INTEGER)') 
    
    c.execute(table) #import table into DB

    
#---------------function that loads in data from csv file 
def load_data():
    try: # tryblock rturns a value everytime the code runs into an exception or not

        data = pd.read_excel('postnummer.xlsx') #reads in csv file
        data.to_sql('postnrtable', conn, if_exists ='replace', index=False) #sends data in sql format into "kundeTable"

        for row in c.execute('SELECT * FROM postnrtable'): #loop that returns ever row in the created table 
           print(row) #prints every single row in DB

    except: #returns when code runs into an exception
        print("Something went wrong while importing data!")
    finally: #returns when code runs without excpetions 
        print("Data has been imported!")



#-------------function that closes the DB
def closeDB():
    conn.close() #closes the db 


#-------------every called function 
main()
createtable()
load_data()
closeDB()


