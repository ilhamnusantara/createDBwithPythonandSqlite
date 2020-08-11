import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Doni','278621','doni@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Noni','8607341','noni@gmail.com')")
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
# print(cursor.fetchall())
print(cursor.fetchone())
print(cursor.fetchone())
for nama, phone, email in cursor:
    print(nama)
    print(phone)
    print(email)
    print('-'*20)
cursor.close()
db.commit()
db.close()