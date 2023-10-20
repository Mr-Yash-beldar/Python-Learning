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

cursor.execute('''Update company set salary =50000 where name="Rushi Patil" ''')

print("\n After Update")
cursor.execute("SELECT * FROM company")
for row in cursor:
    print(row)
    print()
conn.close()
