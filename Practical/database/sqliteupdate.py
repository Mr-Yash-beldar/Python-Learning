import sqlite3

conn= sqlite3.connect('Yash.db')  
print("Connection sucessfull ")

cursor=conn.execute("SELECT * FROM company")
for row in cursor:
   print(row)

conn.execute('''Update company set salary =70000 where name="Rushi Patil" ''')
conn.commit()
print("\nAfter Update: \n")
cursor=conn.execute("SELECT * FROM company")
for row in cursor:
   print(row)


print("Operation successfull")
cursor.close()

