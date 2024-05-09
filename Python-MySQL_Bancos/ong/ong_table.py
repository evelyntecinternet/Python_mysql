import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ong"
)
mycursor = mydb.cursor()

#Criando a tabela usuario
mycursor.execute("CREATE TABLE Usuario (idUsuario int not null auto_increment,nome varchar(45) not null,endereco Varchar(150) not null,email Varchar(100) not null,Primary key(idUsuario))")

#Criando a tabela Ong
mycursor.execute("CREATE TABLE Ong (idOng int not null auto_increment,nome Varchar(45) not null,endereco Varchar(150) not null,email Varchar(100) not null,whatsapp Decimal not null,Primary key(idOng))")

# Criando a tabela Ocorrencia
mycursor.execute("CREATE TABLE Ocorrencia (idOcorrencia int not null auto_increment,data Datetime not null,endereco Varchar(150) not null,descricao Varchar(100) not null,imagem Blob not null,fk_idOng int not null,fk_idUsuario int not null,Primary key(idOcorrencia),Foreign Key (fk_idOng) references Ong (idOng),Foreign Key (fk_idUsuario) references Usuario (idUsuario))")