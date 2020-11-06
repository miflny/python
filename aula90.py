

black = [

]

while True:

    nume = int(input('digite um numero ?? '))
    if nume not in black:
        black.append(nume)
        print('numero adicionado com sucesso ')
    else:
        print('numero duplicado !! não vou adicionar')   

    resp = str(input('Quer continuar [N/S] '))

    if resp in 'Nn':
        break
black.sort()
print(f'os numero digitados foram {black}')