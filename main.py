import sqlite3 as sq
import pandas as pd 
#------------------all imported modules


def main():

    conn = sq.connect('test.db')
    c = conn.cursor()
    data = pd.read_csv('personer.csv')
    data.to_sql('kunder', conn, if_exists= 'replace', index=False)
    c.execute('SELECT * FROM kunder')
    print(c.fetchall())
    conn.commit()
    conn.close()

main()
#---------------------main function 