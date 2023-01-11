import sqlite3 as sq
import pandas as pd 



conn = sq.connect('test.db')

c = conn.cursor()

table =('CREATE TABLE IF NOT EXISTS kundeTable (kundenr TEXT PRIMARY KEY, fname TEXT, ename TEXT, tlf INTEGER, epost TEXT, postnummer INTEGER)')

data = pd.read_csv('personer.csv')

c.execute(table)

data.to_sql('kundeTable', conn, if_exists ='append', index=False)

for row in c.execute('SELECT * FROM kundeTable'):
    print (row)

print(c.fetchall())

conn.close()



