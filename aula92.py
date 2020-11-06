

valores = [


]

while True:
    
    p = int(input('digite um numero ? '))
    
    if p not in valores:
        valores.append(p)
        print('numero adicionado com sucesso ')
    respt = str(input('quer continuar [N/S] ? '))
    if respt in 'Nn':
        break
valores.sort(reverse=True)
print(f'vc digitou {len(valores)} elementos')
print(f'valores digitado foram {valores}')
if 5 in valores:
    print('digito 5 est na lista')
else:
    print('digito 5 não faz parte da lista ')