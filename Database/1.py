import sqlite3

db = sqlite3.connect("Contact.db")
cursor = db.cursor()

sql = """DROP TABLE contacts"""
cursor.execute(sql)
db.commit()

sql = """
        CREATE TABLE IF NOT EXISTS contacts (
        contact_id integer PRIMARY KEY,
        first_name text,
        last_name text,
        email text,
        phone text);"""

cursor.execute(sql)
db.commit()

sql = """
        INSERT INTO contacts (first_name, last_name, email,phone)
        VALUES ('Boris', 'Johnson', 'bj@number10.com', '12345678'),
        ('UKhira', 'Couma', 'uk@203452.com', '910111213');"""

cursor.execute(sql)
db.commit()

sql = "Select * from contacts"
cursor.execute(sql)
print(cursor.fetchall())

sql = "SELECT * FROM contacts WHERE contact_id = 2"
cursor.execute(sql)
print(cursor.fetchone())

sql = "SELECT first_name, last_name FROM contacts ORDER BY last_name Asc;"
cursor.execute(sql)
print(cursor.fetchall())

db.close()



