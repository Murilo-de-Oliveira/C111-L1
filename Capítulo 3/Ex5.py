lista = []

numero = int(input('Digite o número de pessoas: '))

for i in range(numero):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ')
    pessoa = {'nome':nome,'idade':idade,'sexo':sexo}
    lista.append(pessoa)

media = 0
mulheres_20 = 0
for pessoa in lista:
    media += pessoa['idade']
    if (pessoa['sexo'] == 'F' and pessoa['idade'] < 20):
        mulheres_20 += 1

print(f'Média de idades: {media/numero}')
print(f'Mulheres com menos de 20 anos: {mulheres_20}')