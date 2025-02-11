#Exercício 3

continuar = True

while(continuar):
    sexo = input("Insira o sexo: ")
    sexo = sexo.upper()
    if(sexo == "M"):
        print("Masculino")
        continuar = False
    elif(sexo == "F"):
        print("Feminino")
        continuar = False
    else:
        print("Insira um sexo válido")