import sqlite3

conn= sqlite3.connect('Yash.db')  
print("Connection sucessfull ")

cursor=conn.execute("SELECT * FROM company")
for row in cursor:
   print(row)

cursor=conn.execute("SELECT * FROM company")
for row in cursor:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Age:", row[2])
    print("Address:", row[3])
    print("Salary:", row[4])
    print()

conn.commit()
print("Operation successfull")
cursor.close()

