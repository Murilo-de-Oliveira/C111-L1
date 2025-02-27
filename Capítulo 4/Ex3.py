import numpy as np
import random

# Setup do game
tabuleiro = np.zeros([2,2], dtype=int)
linha = random.randint(0, 1)
coluna = random.randint(0, 1)
tabuleiro[linha,coluna] = 1

tabuleiro_legal = (['','']['',''])

for i in range(3):
    print(tabuleiro)
    entrada = input("Digite as coordenadas (linha,coluna): ")
    coordenadas = entrada.split()
    coordenadas = [int(x) for x in coordenadas]
    print(coordenadas)

    if tabuleiro[coordenadas[0],coordenadas[1]] == 1:
        print('Game Over! :( Try Again!')
        print(tabuleiro)
        exit

print('Congratulations! You beat the game! :)')
print(tabuleiro)