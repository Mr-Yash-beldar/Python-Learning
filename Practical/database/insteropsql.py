import sqlite3

conn = sqlite3.connect("Yash.db")
print("Opened database successfully")

conn.execute('''INSERT INTO company (ID, name, age, address, salary)
VALUES (2, 'Yashodip Beldar', 20, '133 Shirpur Maharshtra', 60000.00);''')
print("Record inserted successfully")
conn.execute('''INSERT INTO company (ID, name, age, address, salary)
VALUES (3, 'Harsh jain', 20, 'Chopda,Pankaj Nagar', 65000.00);''')
print("Record inserted successfully")
conn.execute('''INSERT INTO company (ID, name, age, address, salary)
VALUES (4, 'Rushi Patil', 21, 'Shirpur, Kranti Nagar', 70000.00);''')
print("Record inserted successfully")
conn.commit()
conn.close
