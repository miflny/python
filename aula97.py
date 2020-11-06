
galera = []
dado = []
total_maior = 0
total_menor = 0
for contador in range (0,3):
    dado.append(str(input('digite seu nome ? ')))
    dado.append(int(input('digite sua idade ? ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        total_maior = total_maior + 1
        print(f'{pessoa[0]} é maior de idade')
    else:
        total_menor = total_menor + 1
        print(f'{pessoa[0]} é menor de idade')
print(f'temos {total_maior} maiores de idade. é {total_menor} menores de idade.')