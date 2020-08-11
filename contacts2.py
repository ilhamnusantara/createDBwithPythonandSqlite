import sqlite3

db = sqlite3.connect("contacts.sqlite")
for name, hp, email in db.execute("SELECT * from contacts"):
    print(name)
    print(hp)
    print(email)
new_email = "duwida@gmail.com"
phone = input("Masukan nomer handphone : ")
# update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
# lebih aman mengatasi eror seperti dibawah ini
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))
print()
print("Apakah kamu sudah terkoneksi dengan benar : {}".format(update_cursor.connection == db))
print()
update_cursor.connection.commit()
update_cursor.close()
for name, hp, email in db.execute("SELECT * from contacts"):
    print(name)
    print(hp)
    print(email)
db.close()