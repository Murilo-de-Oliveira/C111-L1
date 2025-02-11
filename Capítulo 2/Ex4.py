#Exercício 4

distancia = float(input("Digite a distância em Km: "))

if (distancia <= 200):
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print(f"Distância: {distancia:_.0f} Km")
print(f"Preço: R$ {preco:_.2f}")