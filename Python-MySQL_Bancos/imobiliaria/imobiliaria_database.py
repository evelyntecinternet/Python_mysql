import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

# Para criar a database
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE imobiliaria")