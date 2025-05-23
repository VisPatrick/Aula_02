#   numpy cria um array, que é uma lista de valores, e calcula a média e a mediana
#   Média
#   Mediana pega o valor do meio de uma lista, caso tenha um número par de valores, pega a média dos dois valores do meio
#   Medias de posição ímpares e pares, ou seja, se a lista tiver 5 valores, quartil 1 é o valor 2, quartil 2 é o valor 3, quartil 3 é o valor 4
import numpy as np

dados_salario = [2000, 2500, 3000, 3500, 4000, 30000]

#   CALCULANDO A MÉDIA
media = np.mean(dados_salario)
print('\n', 'Média: ', media)

#   CALCULANDO A MEDIANA
mediana = np.median(dados_salario)
print('\n', 'Mediana: ', mediana)