import psycopg2

conexao = psycopg2.connect(user = 'postgres', 
                           password = '35454913',
                           host = '127.0.0.1',
                           port = '5432',
                           database = 'db_pessoas')

cursor = conexao.cursor()

sql = 'SELECT * FROM pessoas'
cursor.execute(sql)
registro = cursor.fetchall()
print(registro)
cursor.close()
conexao.close()