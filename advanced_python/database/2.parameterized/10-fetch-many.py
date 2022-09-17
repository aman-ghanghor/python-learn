
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
# sql = 'SELECT * FROM student WHERE id>%s'
sql = 'SELECT * FROM student WHERE id>%(id)s'

# params = (100,) 
params = {'id': 100}

try:
    myc.execute(sql, params)
    # fetch rows
    row = myc.fetchone()
    while row is not None:
        print(row)
        row = myc.fetchone()
    print(f"{myc.rowcount} Rows fetched")
except:
    print("Unable to update data")
    conn.rollback()


myc.close()
conn.close()

