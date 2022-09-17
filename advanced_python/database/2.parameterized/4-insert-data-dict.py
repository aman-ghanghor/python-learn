

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
sql = 'INSERT INTO student(name, city) VALUES (%(n)s, %(c)s)' 
params = {'n': 'Manoj', 'c': 'Delhi'}

try:
    myc.execute(sql, params)
    conn.commit()
    print(f"{myc.rowcount} Rows Inserted")
    print(myc.lastrowid)
except:
    print("Unable to insert data")
    conn.rollback()


myc.close()
conn.close()


