

valores = []


mai = 0
men = 0

for posicao in range(0,5):
    valores.append(int(input(f'digite um numero {posicao} : ')))
    
    if posicao == 0:
        mai = men = valores[posicao]
    else:
        if valores[posicao] > mai:
            mai = valores[posicao]
            print(f'maior posicao {mai}')

        if valores[posicao] < men:
            men = valores[posicao]
            print(men)














print(f'vc digitou os numeros {valores} \n')
