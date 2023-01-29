
# Import required libraries
import sqlite3
  
# Connect to SQLite database
# New file created if it doesn't already exist
conn = sqlite3.connect('Geeks.db')
  
# Create cursor object
cursor = conn.cursor()

cursor.execute('PRAGMA foreign_keys = ON')
  
# Create and populate tables
cursor.executescript('''
CREATE TABLE Advisor(
AdvisorID INTEGER NOT NULL,
AdvisorName TEXT NOT NULL,
PRIMARY KEY(AdvisorID)
);
  
CREATE TABLE Student(
StudentID NUMERIC NOT NULL,
StudentName NUMERIC NOT NULL,
AdvisorID INTEGER,
FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
PRIMARY KEY(StudentID)
);
  
INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES
(1,"John Paul"), 
(2,"Anthony Roy"), 
(3,"Raj Shetty"),
(4,"Sam Reeds"),
(5,"Arthur Clintwood");
  
INSERT INTO Student(StudentID, StudentName, AdvisorID) VALUES
(501,"Geek1",1),
(502,"Geek2",1),
(503,"Geek3",3),
(504,"Geek4",2),
(505,"Geek5",4),
(506,"Geek6",2),
(507,"Geek7",2),
(508,"Geek8",3),
(509,"Geek9",NULL),
(510,"Geek10",1);
  
''')

# Query for INNER JOIN
sql = '''SELECT StudentID, StudentName, AdvisorName 
FROM Student 
INNER JOIN Advisor
ON Student.AdvisorID = Advisor.AdvisorID;'''
  
# Executing the query
cursor.execute(sql)
  
# Fetching rows from the result table
result = cursor.fetchall()
for row in result:
    print(row)
  
#Commit changes to database
conn.commit()
  
# Closing the connection
conn.close()