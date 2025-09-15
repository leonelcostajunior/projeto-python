import mysql.connector
from mysql.connector import Error

# Configurações do banco
HOST = "localhost"
USER = "leonel"
PASSWORD = "bianca.2504"
DATABASE = "mysql"  # banco de teste, pode mudar

def conectar_mysql(host, user, password, database=None):
    """Tenta conectar ao MySQL/MariaDB e retorna o objeto de conexão"""
    try:
        conn_params = {
            "host": host,
            "user": user,
            "password": password
        }
        if database:
            conn_params["database"] = database

        conn = mysql.connector.connect(**conn_params)

        if conn.is_connected():
            print(f"Conectado ao MySQL em {host} com sucesso!")
            return conn
        else:
            print("Falha na conexão.")
            return None

    except Error as e:
        print("Erro ao conectar ao MySQL:", e)
        return None

def listar_bancos(conn):
    """Lista todos os bancos disponíveis"""
    try:
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")
        print("\nBancos disponíveis:")
        for db in cursor:
            print("-", db[0])
    except Error as e:
        print("Erro ao listar bancos:", e)

def listar_tabelas(conn, database):
    """Lista todas as tabelas de um banco específico"""
    try:
        cursor = conn.cursor()
        cursor.execute(f"USE {database}")
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        if tables:
            print(f"\nTabelas no banco '{database}':")
            for table in tables:
                print("-", table[0])
        else:
            print(f"\nNenhuma tabela encontrada no banco '{database}'.")
    except Error as e:
        print("Erro ao listar tabelas:", e)

def main():
    print("Script iniciado!\n")
    conn = conectar_mysql(HOST, USER, PASSWORD, DATABASE)
    if conn:
        listar_bancos(conn)
        listar_tabelas(conn, DATABASE)
        conn.close()
        print("\nConexão encerrada.")
    else:
        print("Não foi possível estabelecer a conexão.")

if __name__ == "__main__":
    main()
