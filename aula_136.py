import pymysql

conexao = pymysql.connect(
    host="localhost",
    user="root",
    password=""
    
)

mycursor = conexao.cursor()

mycursor.execute("CREATE DATABASE mydatabase")