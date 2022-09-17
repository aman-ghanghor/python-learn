
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
sql = 'SELECT * FROM student WHERE id>%(id)s'

params = {'id': 100}

try:
    myc.execute(sql, params)
    print(f"{myc.rowcount} Rows Fetched")
    row = myc.fetchone()
    print(row)
except:
    print("Unable to fetch data")
    conn.rollback()


myc.close()
conn.close()

