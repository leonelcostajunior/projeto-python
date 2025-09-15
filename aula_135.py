import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="leonel",
        password="bianca.2504",
        database="mysql"  # você pode colocar qualquer banco existente
    )

    if mydb.is_connected():
        print("Conectado ao MySQL com sucesso!")

        # Listar bancos existentes
        cursor = mydb.cursor()
        cursor.execute("SHOW DATABASES")
        for db in cursor:
            print(db)

except Error as e:
    print("Erro ao conectar ao MySQL:", e)
