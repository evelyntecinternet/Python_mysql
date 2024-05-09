import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="imobiliaria"
)
mycursor = mydb.cursor()

# Criando a tabela Endereco
mycursor.execute("CREATE TABLE Endereco(idEndereco Int not null auto_increment,complemento Varchar(45) not null,bairro Varchar(45) not null,logradouro Varchar(45) not null,estado Varchar(45) not null,cep Int not null,Primary key(idEndereco))")

# Criando a tabela Telefone
mycursor.execute("CREATE TABLE Telefone(idTelefone Int not null auto_increment,ddd Int not null,numero Decimal(9) not null,operadora Varchar(45) not null,Primary key(idTelefone))")

# Criando a tabela Imovel
mycursor.execute("CREATE TABLE Imovel(idImovel Int not null auto_increment,descricao Varchar(150) not null,imagens Blob not null,data Datetime not null,imoveis Varchar(45) not null,fk_idEndereco Int not null,Primary key(idImovel),Foreign Key(fk_idEndereco) References Endereco (idEndereco) )")

# Criando a tabela Pessoa
mycursor.execute("CREATE TABLE Pessoa(idPessoa Int not null auto_increment,nome Varchar(45) not null,cpf Int not null,email Varchar(45) not null,dataNascimento Date not null,fk_idEndereco Int not null,fk_idTelefone Int not null,Primary key(idPessoa),Foreign Key(fk_idEndereco) References Endereco (idEndereco),Foreign Key(fk_idTelefone) References Telefone (idTelefone))")

# Criando a tabela Imobiliaria
mycursor.execute("CREATE TABLE Imobiliaria(idImobiliaria Int not null auto_increment,data Datetime not null,fk_idEndereco Int not null,fk_idTelefone Int not null,fk_idImovel Int not null,Primary key(idImobiliaria),Foreign Key(fk_idEndereco) References Endereco (idEndereco),Foreign Key(fk_idTelefone) References Telefone (idTelefone),Foreign Key(fk_idImovel) References Imovel (idImovel))")