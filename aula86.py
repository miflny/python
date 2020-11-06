

valores = []
mai = 0
men = 0

for posicao in range(0,5):
    valores.append(int(input(f'digite um valor para a posição {posicao} : ')))
    if posicao == 0:
        mai = men = valores[posicao]
    else:
        if valores[posicao] > mai:
            mai = valores[posicao]
           
        if valores[posicao] < men:
            men = valores[posicao]

print(f'vc digitou o valor {valores}')
print(f' maior valor digitado foi {mai} nas posições ',end='')
for indice, numero_ordem in enumerate(valores):
    
    if numero_ordem == mai:
        print(f'{indice}...',end='')
  
print(f'menor valor digitado foi {men} nas posições ',end='')
for indice, numero_ordem in enumerate(valores):

    if numero_ordem == men:
        print(f'{indice}...',end='')