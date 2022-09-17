
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
# sql = 'DELETE FROM student WHERE id=%s'
sql = 'DELETE FROM student WHERE id=%(id)s'

# del_value = (138,)
del_value = {'id': 138}

try:
    myc.execute(sql, del_value)
    conn.commit()
    print(f"{myc.rowcount} Rows Deleted")
except:
    print("Unable to delete data")
    conn.rollback()


myc.close()
conn.close()

