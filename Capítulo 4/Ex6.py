import numpy as np

dataset = np.loadtxt('space.csv', delimiter = ';', dtype=str, encoding='utf-8')

print(dataset[0])
total_linhas, colunas = dataset.shape
linhas = total_linhas - 1 # excluindo a linha de índices

print(f"Linhas: {linhas}, Colunas: {colunas}")

# Exercício 1
missoes = linhas # número de linhas igual ao número de missões
sucesso = np.sum(dataset[1:,7] == 'Success')
porcentagem_sucesso = (sucesso/missoes) * 100
print(f'Porcentagem de sucessos: {porcentagem_sucesso:.2f}%')

# Exercício 2
lista_gastos = dataset[1:,6].astype(float) # converte o tipo de dado para float
gastos = lista_gastos[lista_gastos > 0] # lista de gastos com valores maior que 0
media_gastos = np.mean(gastos) # faz a média dos gastos
print(f'Média dos gastos: U$ {media_gastos:.2f}')

# Exercício 3
lista_eua = dataset[np.char.find(dataset[:,2], "USA") >= 0]
total_eua = len(lista_eua)
print(f'Missões realizadas pelos EUA: {total_eua} missões')

# Exercício 4
lista_spacex = dataset[np.char.find(dataset[:,1], "SpaceX") >= 0]
gastos_spacex = lista_spacex[:,6].astype(float)
maior_gasto = np.max(gastos_spacex)
print(f'Maior gasto da empresa SpaceX: U$ {maior_gasto}')

# Exercício 5
lista_empresas = np.unique(dataset[1:,1], return_counts = True)
print(lista_empresas)
for i in range(len(lista_empresas[0])):
    print(f'Empresa {lista_empresas[0][i]}, Missões: {lista_empresas[1][i]}')

