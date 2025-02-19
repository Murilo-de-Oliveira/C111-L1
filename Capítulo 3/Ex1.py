#Ex 1
times = ['Real Madrid', 'Borussia Dortmund', 'Bayer de Munique', 'Paris Saint German', 'Barcelona']

print(f'Primeiros colocados: {times[:4]}')
print(f'Últimos colocados: {times[-2:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'Posição do Barcelona: {times.index('Barcelona')}')