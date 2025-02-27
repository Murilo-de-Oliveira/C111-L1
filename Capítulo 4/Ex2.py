import numpy as np

array_0_51 = np.arange(0, 51, 2)
array_100_50 = np.arange(50, 100, 2)
array_100_50 = array_100_50[::-1] # revertendo o array

array_concat = np.concatenate((array_0_51,array_100_50))

print(array_0_51)
print(array_100_50)
print(array_concat)
