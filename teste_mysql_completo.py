import mysql.connector
from mysql.connector import Error
print("Script iniciado!")


# Configurações do banco
HOST = "localhost"          # Host do MySQL
USER = "leonel"             # Usuário
PASSWORD = "bianca.2504"    # Senha
DATABASE = "mysql"          # Banco padrão para teste

def conectar_mysql(host, user, password, database):
    """Tenta conectar ao MySQL e retorna o objeto de conexão"""
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if conn.is_connected():
            print(f"Conectado ao MySQL em {host} com sucesso!")
            return conn
        else:
            print("Falha ao conectar, conexão não estabelecida.")
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
    conn = conectar_mysql(HOST, USER, PASSWORD, DATABASE)
    if conn:
        listar_bancos(conn)
        listar_tabelas(conn, DATABASE)
        conn.close()
        print("\nConexão encerrada.")

if __name__ == "__main__":
    main()
