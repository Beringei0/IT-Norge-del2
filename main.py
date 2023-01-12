import sqlite3 as sq
import pandas as pd 
#-------------------every imported module 


#-------------------function that creates DB
def createtable():
    global conn #makes the var "conn" global 
    
    
    conn = sq.connect('kunder.db') #creates a DB


#------------main function
def main():
    global c
    
    #creates a new table with column "kundenr" as primary
    table =('CREATE TABLE IF NOT EXISTS kundeTable (kundenr TEXT PRIMARY KEY, fname TEXT, ename TEXT, tlf INTEGER, postnummer INTEGER)') 

    c = conn.cursor() #makes a cursor

    c.execute(table) #import table into DB

    for row in c.execute('SELECT * FROM kundeTable'): #loop that returns ever row in the created table 
        print(row)


#---------------function that loads in data from csv file 
def load_data():
    try: # tryblock rturns a value everytime the code runs into an exception or not 
        data = pd.read_csv('personer.csv') #reads in csv file

        data.to_sql('kundeTable', conn, if_exists ='replace', index=False) #sends data in sql format into "kundeTable"

        conn.close() # closes the DB 
    except: #returns when code runs into an exception
        print("Something went wrong while importing data!")
    finally: #returns when code runs without excpetions 
        print("Data has been succesfully imported!")


#-------------every called function 
createtable()
main()
load_data()
