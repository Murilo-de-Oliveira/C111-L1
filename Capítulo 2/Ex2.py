#Exercício 2

numero = int(input("Insira um número para mostrar sua tabuáda: "))
limite = int(input("Insira até que número a tabuáda deve aparecer: "))

for i in range(limite+1):
    print(f"{numero} x {i}: {numero * i}")
