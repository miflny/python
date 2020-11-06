

valor = []

maior = 0
menor = 0
for contador in range(0,5):
    valor.append(int(input(f'digite um valor na posição {contador} : ')))

    if contador == 0:
        maior = menor = valor[contador]
    else:
        if valor[contador] > maior:
            maior = valor[contador]

        if valor[contador] < menor:
            menor = valor[contador]

print(f'valor digitador {valor}')
print(f'maior valor digitador {maior} nas posições ',end='')
for i, n in enumerate(valor):
    if n == maior:
        print(f'{i}...',end='')
print()       
print(f'menor valor digitado {menor} nas posições ',end='')
for i,n in enumerate(valor):
    if n == menor:
        print(f'{i}...',end='')




