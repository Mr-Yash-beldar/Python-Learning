import sqlite3

conn=sqlite3.connect("Yash.db")
print("Opened database successfully")

conn.execute('''create table company(ID int primary key not null,
             name text not null,
             age int not null,
             address char(50),
             salary real
             );''')
print("table created successfully")