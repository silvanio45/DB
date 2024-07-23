import psycopg2

conexao = psycopg2.connect(user = 'postgres', 
                           password = '35454913',
                           host = '127.0.0.1',
                           port = '5432',
                           database = 'db_pessoas')

cursor = conexao.cursor()

sql = 'UPDATE pessoas SET nome=%s, apelido=%s, idade=%s WHERE idpessoas=%s'

nome = input('informe o nome: ')
apelido = input('informe o apelido: ')
idade = input('informe a idade: ')
idpessoa = input('informe o id da pessoa: ')

data = (nome, apelido, idade, idpessoa)
cursor.execute(sql, data)
conexao.commit()

registros = cursor.rowcount
print(f'registros: {registros}')

cursor.close()
conexao.close()