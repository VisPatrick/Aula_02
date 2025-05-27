import pandas as pd
import numpy as np

df = pd.read_excel('./aula02/vendas_roupas.xlsx')
print('\n', df.head(10))  # Exibe as 5 primeiras linhas do DataFrame
# print(df.describe())

categoria = df['Categoria']
quantidade_vendida = df['Unidades Vendidas']

media = np.mean(quantidade_vendida)
print(f'\nMédia: {media:.2f}')
mediana = np.median(quantidade_vendida)
print(f'Mediana: {mediana:.2f}')
print(20* '-')

quantidade_organizada = df.sort_values(by='Unidades Vendidas', ascending=False) # Organiza os dados
# print(quantidade_organizada)

print(quantidade_vendida.values)

satisfacao = df[df['Satisfação'] == 'Baixo']
print(satisfacao)

