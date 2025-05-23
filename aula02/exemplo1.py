#   uma serie é facilmente confundida com uma lista   # uma lista é uma coleção de dados
#   uma série é uma coluna de dados
#   DataSet termo generico para um conjunto de dados para qualquer coleçãode dados   #dataFrame estrutura de dados específica do pandas
#   DataFrame é uma estrutura de dados bidimensional, semelhante a uma tabela, onde os dados são organizados em linhas e colunas.
#   media é a soma dos valores dividida pelo número de valores

import pandas as pd

data = {
    'Nome': ['Ana', 'João', 'Maria'],
    'Idade': [23, 35, 29],
    'Gênero': ['F', 'M', 'F'],
    'Altura': [1.70, 1.80, 1.75]
}

#   print(data['nome']) # imprime a coluna nome
df_dados = pd.DataFrame(data)
print('\n', df_dados)
print('\nVAEIÁVEIS QUANTITATIVAS')
print(30*'=')

#   PRINTANDO VARIÁVEIS QUANTITATIVAS #  QUANTITATIVAS SÃO AS QUE SÃO NÚMEROS
print('Exibindo Idade: ')
print(df_dados['Idade']) 

print('\nExibindo Altura: ')
print(df_dados['Altura'])

#   PRINTANDO VARIÁVEIS QUALITATIVAS #  QUALITATIVAS SÃO AS QUE NÃO SÃO NÚMEROS
print(30*'=')

print('\nExibindo Nome: ')
print(df_dados['Nome'])

print('\nExibindo Gênero: ')
print(df_dados['Gênero'])
