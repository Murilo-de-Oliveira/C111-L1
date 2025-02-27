import numpy as np

np.random.seed(10)

tabela = np.random.randint(1,51,[4,4])

print(tabela)

media_colunas = tabela.sum(axis=0)/4
media_linhas = tabela.sum(axis=1)/4

print(f"Média das colunas: {media_colunas}") #soma das colunas e média
print(f"Média das linhas: {media_linhas}") #soma das linhas e média

print(f"Maior média das colunas: {max(media_colunas)}")
print(f"Maior média das linhas: {max(media_linhas)}")

elementos = np.unique(tabela, return_counts = True)[0]
frequencia = np.unique(tabela, return_counts = True)[1]

elementos_repetidos = []

for i in range(len(frequencia)):
    if frequencia[i] >= 2:
        elementos_repetidos.append(int(elementos[i]))

print(f"Elementos repetidos: {elementos_repetidos}")



