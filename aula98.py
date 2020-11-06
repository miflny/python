
galera = [

]
dado =[

]
mai = 0
men = 0

while True:
    galera.append(str(input('Nome : ')))
    galera.append(float(input('Peso : ')))
    if len(dado) == 0:
        mai = men = galera[1]
    else:
        if galera[1] > mai:
            mai = galera[1]
        if galera[1] < men:
            men = galera[1]

    dado.append(galera[:])
    galera.clear()
    
    resp = str(input('quer continuar [N/S]'))
    if resp in 'Nn':
        break

print('=' * 30)
print(f' maior peso foi de {mai} KG peso de ',end='')

for pessoa in dado:
    if pessoa[1] == mai:
        print(f' [{pessoa[0]}] ',end='')
print()
print(f'menor peso foi de {men} KG peso de ',end='')
for pessoa in dado: 
    if pessoa[1] == men:
        print(f'[{pessoa[0]}]',end='') 
        print()      
print(f'ao todo vc cadrastrou {len(dado)} pessoas')