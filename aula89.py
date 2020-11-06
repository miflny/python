

blacklist = []

while True:
    num = int(input('digite um valor '))
    if num not in blacklist:
        blacklist.append(num)
        print('numero adicionado com sucesso ')
    else:
        print('numero duplicado ! não vou adicionar ')

    resposta = str(input('Quer continuar ?? [N/S] '))
    
    if resposta in 'Nn':
        break
blacklist.sort()
print(f'os numero que vc digitou são {blacklist}')