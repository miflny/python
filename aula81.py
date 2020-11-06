

from random import randint

print('=========================================================')
print('os numeros sorteados fora ')
p = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
for indice in p:
    print(f'{indice}', end=' ')
  

print('\n=========================================================')
print(f'o maior numero foi {max(p)}')
print(f'o menor numero foi {min(p)}')
print('===========================================================')