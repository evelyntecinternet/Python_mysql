import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="rifa"
)

mycursor = mydb.cursor()

# Criando tabela usuario
mycursor.execute("CREATE TABLE usuario (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#Criando tabela rifa
mycursor.execute("CREATE TABLE rifa (idrifa int not null auto_increment,data datetime not null, dia date not null,hora time not null, premio float not null,numeros int not null,valor_numero float not null,descricao varchar(100),fk_idCriador int not null,Primary key(idrifa),Foreign key(fk_idCriador) references Usuario (idUsuario))")

#Criando tabela numeros_vendidos
mycursor.execute("CREATE TABLE numeros_vendidos (idnumeros_vendidos int not null auto_increment,numero_escolhido int not null,fk_idrifa int not null,fk_idusuario int not null,Primary key(idnumeros_vendidos),Foreign Key (fk_idrifa) references rifa (idrifa),Foreign Key (fk_idusuario) references usuario (idusuario))")