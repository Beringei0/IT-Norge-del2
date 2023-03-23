import sqlite3

# Connect to the database
conn = sqlite3.connect('test.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the Name table
cursor.execute('''
CREATE TABLE Name (
  kundenr INTEGER NOT NULL PRIMARY KEY,
  fname TEXT NOT NULL,
  age TEXT NOT NULL,
  email TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
