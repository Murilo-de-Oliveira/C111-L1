import numpy as np

array_de_uns = np.ones(8)
array_random = np.random.randint(0, 10, 8)
array_soma = array_de_uns + array_random

soma = array_soma.sum()

if soma >= 40:
    array_reshape = np.reshape(array_soma, [4,2])
else:
    array_reshape = np.reshape(array_soma, [2,4])

print(f"Array de uns: {array_de_uns}")
print(f"Array aleatório: {array_random}")
print(f"Soma dos arrays: {array_soma}")
print(f"Soma dos arrays: {soma}")
print(f"Resultado da patifaria: {array_reshape}")
