nomes = []
pesos = []

for i in range(3):
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso: '))
    nomes.append(nome)
    pesos.append(peso)

mais_pesado = pesos.index(max(pesos))
mais_leve = pesos.index(min(pesos))

print(f'Pessoa mais pesada: {nomes[mais_pesado]}')
print(f'Pessoa mais leve: {nomes[mais_leve]}')
