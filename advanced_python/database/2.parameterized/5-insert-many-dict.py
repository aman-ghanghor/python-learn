

import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        username='root',
        password='Aman@1234',
        database='mydb'
    )
    print("Connected Successfully")
except:
    print("Unable to Connect")

myc = conn.cursor()
sql = 'INSERT INTO student(name, city) VALUES (%(name)s, %(city)s)'
seq_of_params = [
    {'name': 'Santosh', 'city': 'Delhi'},
    {'name': 'Manoj', 'city': 'Mumbai'},
    {'name': 'Kamal', 'city': 'Indore'}]

try:
    myc.executemany(sql, seq_of_params)
    conn.commit()
    print(f"{myc.rowcount} Rows Inserted")
    print(myc.lastrowid)
except:
    print("Unable to insert data")


myc.close()
conn.close()
