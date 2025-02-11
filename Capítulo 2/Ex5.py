#Exercício 5

numero_invalido = True

while(numero_invalido):
    numero = (input("Insira um número entre 1000 e 9999: "))
    if(int(numero) > 1000 or int(numero) < 10000):
        numero_invalido = False

numeros = numero.strip()
print("Número: " + numero)
print("Unidade: " + numeros[3])
print("Dezena: " + numeros[2])
print("Centena: " + numeros[1])
print("Milhar: " + numeros[0])