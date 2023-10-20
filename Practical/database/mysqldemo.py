import mysql.connector

conn = mysql.connector.connect(
    host="localhost",  
    user="root",  
    password="",  
    database="python_practical"  
)


cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE company (
        ID INT PRIMARY KEY NOT NULL,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        address VARCHAR(50),
        salary FLOAT
    )
''')
print("Table created successfully")

# Insert records
cursor.execute("INSERT INTO company (ID, name, age, address, salary) VALUES (2, 'Yashodip Beldar', 20, '133 Shirpur Maharashtra', 60000.00)")
cursor.execute("INSERT INTO company (ID, name, age, address, salary) VALUES (3, 'Harsh Jain', 20, 'Chopda, Pankaj Nagar', 65000.00)")
cursor.execute("INSERT INTO company (ID, name, age, address, salary) VALUES (4, 'Rushi Patil', 21, 'Shirpur, Kranti Nagar', 70000.00)")
conn.commit()
print("Records inserted successfully")

# Retrieve records
cursor.execute("SELECT * FROM company")
for row in cursor:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Age:", row[2])
    print("Address:", row[3])
    print("Salary:", row[4])
    print()

# Close the cursor and connection
cursor.close()
conn.close()
