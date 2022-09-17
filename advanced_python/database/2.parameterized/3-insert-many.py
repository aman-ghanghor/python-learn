#  ================= executemany() Method =================
#
#  This method is used to prepare given SQL query and executes it against all parameter
#  sequences or mapping found in the sequence seq_of_params.
#
#  With the executemany() method it is possible to specify multiple statements to 
#  execute in the sql argument
#
#  Syntax:-   cursor_object.executemany(sql, seq_of_params)
#
#  sql = It is sql query.
#
#  seq_of_params = It is a list of tuples, containing the data to insert.




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
sql = 'INSERT INTO student(name, city) VALUES (%s, %s)' 
seq_of_params = [('Deepak', 'Indore'), ('Roshini', 'Mumbai'), ('Jack', 'London')]

try:
    myc.executemany(sql, seq_of_params)
    conn.commit()
    print(f"{myc.rowcount} Rows Inserted")
    print(myc.lastrowid)
except:
    print("Unable to insert data")


myc.close()
conn.close()


