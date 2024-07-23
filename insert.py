import psycopg2

conexao = psycopg2.connect(user = 'postgres', 
                           password = '35454913',
                           host = '127.0.0.1',
                           port = '5432',
                           database = 'db_pessoas')

cursor = conexao.cursor()

sql = 'INSERT INTO pessoas (nome, apelido, idade) VALUES(%s, %s,%s)'

nome = input('Informe o nome: ')
apelido = input('informe o apelido: ')
idade = input('informe a idade: ')

dados = (nome, apelido, idade)
cursor.execute(sql, dados)
conexao.commit()

registros = cursor.rowcount
print(f'registros: {registros}')

cursor.close()
conexao.close()