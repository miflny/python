
valor = []

maior = 0
menor = 0
for posicao in range (0,5):
    valor.append(int(input(f'digite um numero {posicao} : ')))

    if posicao == 0:
        maior = menor = valor[posicao]
    else:
        if valor[posicao] > maior:
            maior = valor[posicao]
        if valor[posicao] < menor:
            menor = valor[posicao]
print(f'vc digitou os numeros {valor}')      
print(f'O maior valor digitado {maior} na posicao ',end='')

for item, numero_odem in enumerate(valor):
    if numero_odem == maior:
        print(f'{item}...',end='')
        print()

print(f'O menor valor digitado {menor} na posicao ',end='')
for item, numero_odem in enumerate(valor):
    if numero_odem == menor:
        print(f'{item}..',end='')
        print()