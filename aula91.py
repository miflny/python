

blacklist = [

]

while True:
    numero = int(input('digite um valor ? '))
    if numero not in blacklist:
        blacklist.append(numero)
        print('numero adicionado com sucesso')

    else:
        print('numero duplicado !! não vou adicionar ')
    res = str(input('quer continuar ? [N/S]' ))
    if res in 'Nn':
        break

print(f'os numeros digitados foram {blacklist}')
