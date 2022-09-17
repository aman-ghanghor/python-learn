
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
sql = 'UPDATE student SET name=%s, city=%s WHERE id=%s'

params = ('Pawan', 'Kanpur', 139) 

try:
    myc.execute(sql, params)
    conn.commit()
    print(f"{myc.rowcount} Rows Updated")
except:
    print("Unable to update data")
    conn.rollback()


myc.close()
conn.close()

