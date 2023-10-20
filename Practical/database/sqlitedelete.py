import sqlite3

conn= sqlite3.connect('Yash.db')  
print("Connection sucessfull ")

cursor=conn.execute("SELECT * FROM company")
for row in cursor:
   print(row)

name_to_delete = input("Enter name to delete from database: ")

cursor.execute("DELETE FROM company WHERE name = ?", (name_to_delete,))

print("\nAfter Update: \n")

cursor=conn.execute("SELECT * FROM company")
for row in cursor:
   print(row)


print("Operation successfull")
cursor.close()

