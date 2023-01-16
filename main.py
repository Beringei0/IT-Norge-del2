import sqlite3 as sq
import pandas as pd 
#-------------------every imported module 


#------------main function
def main():
    global conn #makes the var "conn" global 
    global c #makes the var "c" global 

    conn = sq.connect('kunder.db') #creates a DB

    c = conn.cursor() #makes a cursor


#-------------------function that creates DB
def createtable():

    #creates a new table with column "kundenr" as primary
    table =('CREATE TABLE IF NOT EXISTS kundeTable (kundenr TEXT PRIMARY KEY, fname TEXT, ename TEXT, epost TEXT, tlf INTEGER, postnummer INTEGER)') 
    
    c.execute(table) #import table into DB

    
#---------------function that loads in data from csv file 
def load_data():

        data = pd.read_csv('personer.csv') #reads in csv file
        data.to_sql('kundeTable', conn, if_exists ='append', index=False) #sends data in sql format into "kundeTable"

    



#-------------function that closes the DB
def closeDB():
    conn.close() #closes the db 


#-------------every called function 
main()
createtable()
load_data()
closeDB()


