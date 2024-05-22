import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customer WHERE id = 'x'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")