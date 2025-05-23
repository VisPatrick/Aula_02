import numpy as np

idade = np.array([35, 25, 38, 31, 45, 22, 36, 29, 40, 32])

q1 = np.quantile(idade, 0.25)
q2 = np.quantile(idade, 0.50)
q3 = np.quantile(idade, 0.75)

print(f'\nQ1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')

#   CALCULO DA MÉDIA E MEDIANA
media = np.mean(idade)
print(f'Média: {media}')
mediana = np.median(idade)
print(f'Mediana: {mediana}')
print(10* '-')