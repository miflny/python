
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(f'matriz {matriz}')

print('matriz emprima de outra forma : ')

for lista in matriz:
    for elemento in lista:
        print([elemento], end=' ')
    print()