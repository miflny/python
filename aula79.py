
listagem = ('lapis',1.75,
            'borracha',2.00,
            'caderno',15.90,
            'estojo',25.00,
            'transferidor',4.20,
            'compasso',9.99,
            'mochila',120.32,
            'caneta',22.30,
            'livro',34.90,)

print('-'* 40)
print(f'{"LISTAGEM DE PREÇO" :^40}')
print('-'* 40)

for posicao in range(0,len(listagem)):
    
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}',end='')
    else:
        print(f'R$ {listagem[posicao]:>5.2f}')
print('-'* 40)