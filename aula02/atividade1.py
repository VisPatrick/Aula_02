import numpy     as np

VALORES_VENDAS = np.array([150000, 180000, 200000, 220000, 250000, 280000, 300000, 320000, 400000, 1500000])

#   Valor medio
media = np.mean(VALORES_VENDAS)
print(f'\nMédia: {media:.2f}')
#   Valor mediano
mediana = np.median(VALORES_VENDAS)
print(f'Mediana: {mediana:.2f}')
print(20* '-')