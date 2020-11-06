

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

spar = 0
mai = 0
scol = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz [linha] [coluna] = int(input(f'digite um numero [{linha} , {coluna}] : '))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz [linha] [coluna]:^5}]',end='')
        if matriz [linha] [coluna] % 2 == 0:
            spar += matriz [linha] [coluna]
    print()
print('='*35)
print(f'A soma de todos os pares é {spar}')
for coluna in range(0,3):
    scol += matriz [coluna] [2]
print(f'a soma da terceira coluna é {scol}')
for coluna in range(0,3):
    if matriz [1] [coluna] == 0:
        mai = matriz [1] [coluna]
    elif matriz [1] [coluna] > mai:
        mai = matriz [1] [coluna]
print(f'maior numero da segunda coluna é {mai}')
            

     