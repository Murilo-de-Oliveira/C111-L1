
loja1 = {'iPhone 16 Pro Max', 'OnePlus 13', 'Google Pixel 9 Pro', 'Samsung Galaxy S24 Ultra', 'Apple iPhone 16 Plus', 'Google Pixel 8a', 'iPhone 15', 'Samsung Galaxy Z Fold 6'}
loja2 = {'Samsung Galaxy S24 Ultra', 'OnePlus 12', 'iPhone 15 Pro Max', 'Xiaomi 14 Ultra', 'Samsung Galaxy Z Flip 6', 'Google Pixel 9 Pro XL', 'Google Pixel 7a'}

print(f'Modelos da Loja 1: {loja1}')
print(f'Modelos da Loja 2: {loja2}')

print(f'Total de modelos da Loja 1: {len(loja1)}')
print(f'Total de modelos da Loja 2: {len(loja2)}')

print(f'Modelos disponíveis nas duas lojas: {loja1.intersection(loja2)}')
