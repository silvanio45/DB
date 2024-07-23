import psycopg2

conexao = psycopg2.connect(user = 'postgres', 
                           password = '35454913',
                           host = '127.0.0.1',
                           port = '5432',
                           database = 'db_pessoas')

cursor = conexao.cursor()

sql = 'DELETE FROM pessoas WHERE idpessoas=%s'
idpessoas = input('Informe o registro da pessoa que será eliminada: ')

cursor.execute(sql,idpessoas)
conexao.commit()

registros = cursor.rowcount
print(f'registros: {registros}')

cursor.close()
conexao.close()