import sqlite3 as sq
import pandas as pd 
#------------------all imported modules


def main():

    conn = sq.connect('test.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS test (fname TEXT(20), ename TEXT(40), epost TEXT, tlf INTEGER(20), postnummer INTEGER(4))')
    data = pd.read_csv('personer.csv')
    data.to_sql('data', conn, if_exists= 'replace', index=False)
    c.execute('SELECT * FROM test')
    print(c.fetchall())
    conn.commit()
    conn.close()

main()
#---------------------main function 