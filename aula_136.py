import pymysql

conexao = pymysql.connect(
    host="localhost",
    user="root",
    password=""
    
)

mycursor = conexao.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:

    print(x)
