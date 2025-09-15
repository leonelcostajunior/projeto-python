import pymysql

conexao = pymysql.Connect(

    host = "localhost",
    user = "root",
    password = "",
    database= "mydatabase"
)

mycursor = conexao.cursor()

#sql = """
#CREATE TABLE pessoas (
#     nome VARCHAR(255), 
#     idade INT(2)
# )
# """

# mycursor.execute(sql)
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)