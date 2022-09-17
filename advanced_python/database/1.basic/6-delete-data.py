
#  Create Connection



import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='Aman@1234',
        host='localhost',
        port='3306',
        database='mydb'
    )
    print("Connected")
except:
    print('Unable to connect')


myc = conn.cursor()
sql = "DELETE FROM student WHERE name='Krishna' "

try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount, "Rows Deleted")
except:
    conn.rollback()
    print("Rollback")


myc.close()
conn.close()



