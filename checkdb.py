import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Tolong masukkan nama yang anda cari : ")

# for row in conn.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

conn.close()