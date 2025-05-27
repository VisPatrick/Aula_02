import pandas as pd

df = pd.read_excel('./aula02/vendas_eletronicos.xlsx')
print('\n', df.head())  # Exibe as 5 primeiras linhas do DataFrame

# Exibe o maior valor da coluna 'Faturamento Total'
print('\nMaaior valor de faturamento total: ')
print(df['Faturamento Total (R$)'].max())

# Exibe o menor valor da coluna 'Faturamento Total'
print('\nMenor valor de faturamento: ')
print(df['Faturamento Total (R$)'].min())

#   CALCULANDO TOTAL DE UNIDADES VENDIDAS
print('\nTotal de unidades vendidas: ')
print(df['Unidades Vendidas'].sum())

#   CALCULANDO MÉDIA DOS PREÇOS POR UNIDADE
print('\nMédia dos preços por unidade: ')
print(df['Preço por Unidade (R$)'].mean())