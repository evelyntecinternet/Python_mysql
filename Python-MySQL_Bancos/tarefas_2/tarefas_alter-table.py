import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Tarefas_2"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE tarefas ADD COLUMN data date not null")