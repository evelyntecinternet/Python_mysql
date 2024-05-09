import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="barbearia"
)
mycursor = mydb.cursor()

# Criando a tabela Cliente
mycursor.execute("CREATE TABLE Cliente(idCliente int not null auto_increment,nome Varchar(45) not null,dataNascimento Date not null,whatsapp Decimal(9) not null,Primary key(idCliente))")

# Criando a tabela Servico
mycursor.execute("CREATE TABLE Servico(idServico int not null auto_increment,nome Varchar(45) not null,valor Float not null,descricao Varchar(100),Primary key(idServico))")

# Criando a tabela Agenda
mycursor.execute("CREATE TABLE Agenda(idAgenda int not null auto_increment,data Datetime not null,dia Date not null,hora Time not null,pago Char(1),fk_idCliente Int not null,fk_idServico Int not null,Primary Key(idAgenda),Foreign key(fk_idCliente) References Cliente (idCliente),Foreign key(fk_idServico) References Servico (idServico))")