import sqlite3                          #Import sqlite3 library

db = sqlite3.connect("film.db")         #Create Connection object
cursor = db.cursor()                    #Create Cursor object

#Create a String to hold SQL query
sql = """
    CREATE TABLE IF NOT EXISTS Films
    (FilmID integer PRIMARY KEY,
    Title text,
    Genre text.
    Year integer);"""

cursor.execute(sql)
db.commit()                             
