import mysql.connector
from mysql.connector import Error

# Configurações do banco
HOST = "localhost"
USER = "leonel"
PASSWORD = "bianca.2504"
DATABASE = "mysql"  # banco de teste, pode mudar

print("Script iniciado!")

# Teste da importação
try:
    print("Tentando importar mysql.connector... OK")
except Exception as e:
    print("Erro na importação:", e)

# Tentativa de conexão
try:
    print("Tentando conectar ao MySQL...")
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=mysql
    )
    if mydb.is_connected():
        print("Conectado ao MySQL com sucesso!")
    else:
        print("Falha na conexão: mydb.is_connected() retornou False")
except Error as e:
    print("Erro ao conectar ao MySQL:", e)
    mydb = None

# Listar bancos
if mydb:
    try:
        cursor = mydb.cursor()
        cursor.execute("SHOW DATABASES")
        print("\nBancos disponíveis:")
        for db in cursor:
            print("-", db[0])
    except Error as e:
        print("Erro ao listar bancos:", e)

# Listar tabelas do banco escolhido
if mydb:
    try:
        cursor.execute(f"USE {DATABASE}")
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        if tables:
            print(f"\nTabelas no banco '{DATABASE}':")
            for table in tables:
                print("-", table[0])
        else:
            print(f"\nNenhuma tabela encontrada no banco '{DATABASE}'")
    except Error as e:
        print("Erro ao listar tabelas:", e)

# Encerramento da conexão
if mydb:
    mydb.close()
    print("\nConexão encerrada.")
else:
    print("\nNenhuma conexão foi estabelecida.")
