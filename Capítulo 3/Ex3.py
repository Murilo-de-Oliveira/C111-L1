
nome = input('Digite seu nome: ')
media = float(input('Digite sua média: '))

aluno = {'nome':nome,'média':media}

if aluno['média'] >= 50:
    sit = 'AP'
else:
    sit = 'RP'

aluno['situação'] = sit

print(aluno.items())
