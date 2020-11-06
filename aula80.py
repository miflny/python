from random import randint

numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('==============================================')
print('================================================')
print('os valores sorteado foram : ',end=' ')
for indice in numeros:
    print(f'{indice} ',end=' ')
print('\n==============================================')
print(f'o maior valor sorteado foi : {max(numeros)}')
print(f'o menor valor sorteado foi : {min(numeros)}')
print('================================================')
print('================================================')