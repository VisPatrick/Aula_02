import pandas as pd
import numpy as np

df = pd.read_excel('./aula02/vendas_roupas.xlsx')
print('\n', df.head(10))  # Exibe as 5 primeiras linhas do DataFrame
# print(df.describe())

categoria = df['Categoria']