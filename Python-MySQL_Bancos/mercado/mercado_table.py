import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mercado"
)
mycursor = mydb.cursor()

# Criando a tabela produtos
mycursor.execute("Create TABLE Produtos (idProdutos int not null auto_increment,nome varchar(45) not null,quantidade int not null,valor_unitario float not null,Primary key(idProdutos)) ")

#Criando a tabela Venda
mycursor.execute("Create TABLE Venda (idVenda int not null auto_increment,data_venda datetime not null,valor_total float not null,Primary Key(idVenda))")

#Criando a tabela itens_vendidos
mycursor.execute("Create TABLE itens_vendidos (iditens_vendidos int not null auto_increment,valor_venda float not null,quantidade int not null,fk_idVenda int not null,fk_idProdutos int not null,Primary key(iditens_vendidos),Foreign key(fk_idVenda) references Venda (idVenda),Foreign key(fk_idProdutos) references Produtos (idProdutos))")