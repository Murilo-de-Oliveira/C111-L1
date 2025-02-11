#Exercício 1
nome = "Murilo de Oliveira Domingos Figueiredo"

#Nome com letras maiúsculas
print(f"Nome com letras maiúsculas: {nome.upper()}")

#Nome com letras minúsculas
print(f"Nome com letras minúsculas: {nome.lower()}")

#Número de letras no nome
nome_sem_espaco = nome.replace(" ", "")
print(f"Total de letras no nome: {len(nome_sem_espaco)}")

#Nome com "do Inatel" no final
nome_split = nome.split(" ")
nome_concatenado = nome_split[0]
for i in range(1,len(nome_split)-1):
    nome_concatenado = nome_concatenado + " " + nome_split[i]
nome_concatenado = nome_concatenado + " do Inatel"
print(f"Último nome como do Inatel: {nome_concatenado}")