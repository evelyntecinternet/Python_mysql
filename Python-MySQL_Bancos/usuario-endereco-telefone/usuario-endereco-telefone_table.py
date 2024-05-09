import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="usuario_endereco_telefone"
)
mycursor = mydb.cursor()

#Criando a tabela Endereco
#mycursor.execute("CREATE TABLE Endereco(idEndereco int not null auto_increment,logradouro Varchar(45) not null,bairro Varchar(45) not null,estado Varchar(45) not null,complemento Varchar(45) not null,cep Int not null, Primary Key(idEndereco))")

#Criando a tabela Pessoa
#mycursor.execute("CREATE TABLE Pessoa(idPessoa int not null auto_increment,nome Varchar(45) not null,numero_casa Varchar(20) not null,data_nascimento Date not null,sexo Varchar(2),cpf Int not null,fk_idEndereco Int not null,Primary key(idPessoa),Foreign key(fk_idEndereco) References Endereco (idEndereco) )")

# Criando a tabela Telefone
mycursor.execute("CREATE TABLE Telefone(idTelefone int not null auto_increment,numero Decimal(9) not null,operadora Varchar(45) not null,ddd Int not null,fk_idPessoa Int not null,Primary key(idTelefone),Foreign key(fk_idPessoa) References Pessoa (idPessoa) )")