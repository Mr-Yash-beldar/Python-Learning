import mysql.connector

conn = mysql.connector.connect(
    host="localhost",  
    user="root",  
    password="",  
    database="python_practical"  
)


cursor = conn.cursor()


# Before Update
cursor.execute("SELECT * FROM company")
for row in cursor:
    print(row)
    print()

name_to_delete = input("Enter name to delete from database: ")

cursor.execute("DELETE FROM company WHERE name = %s", (name_to_delete,))

print("\n After Update\n")
cursor.execute("SELECT * FROM company")
for row in cursor:
    print(row)
    print()
conn.close()
