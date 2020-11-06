
valores = []

for conte in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {conte} : ')))
print('=============================================================')
print('=============================================================')
print(f'vc digitou os valores {valores}')

for indice , numero in enumerate(valores):
    print(f'na posição {indice} encotrei o numero {numero} ')
