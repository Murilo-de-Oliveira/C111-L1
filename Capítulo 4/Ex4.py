import numpy as np

#np.random.seed(10)

tabela = np.random.randint(0,1,size=([np.random.randint(1,10),np.random.randint(1,10)]))

print(tabela)
print(tabela.shape)

linhas, colunas = tabela.shape

if (linhas * colunas & 1):
    print("Vetor unidimensional ímpar")

else: 
    print("Vetor unidimensional par")