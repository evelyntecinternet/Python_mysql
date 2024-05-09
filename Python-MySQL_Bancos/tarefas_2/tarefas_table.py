import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Tarefas_2"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE tarefas(idtarefas int not null auto_increment,nome varchar(45) not null,descricao varchar(100) not null,status char(1), Primary key(idtarefas))")