

print('=============LOJAS MIFLNY=============')


produto = float(input('Preço das compras: R$ '))

print('FORMAS DE PAGAMENTO')

print(''' 
    [1] á vista dinheiro/cheque
    [2] á vista no cartão
    [3] 2x no cartão
    [4] 3x ou mais no cartão
    [5] sair do programa
    ''')

opção = int(input('Qual é a opção ?? '))
    
if opção == 1:
    desconto_dinheiro = produto - (produto * 10 / 100) 
    print(desconto_dinheiro)
elif opção == 2:
    avista_cartão = produto - (produto * 5 / 100)
    print(avista_cartão)
elif opção == 3:
    parcela = int(input('quantas parcelas ?? '))
    cartãox2 = produto / parcela
    print('sua compra sera parecelada em {}x de {} sem juros'.format(parcela,cartãox2))
    print('sua compra de R$ {}'.format(produto))
elif opção == 4:
    
    parcela = int(input('quantas parcelas ?? '))
    maisde3 = produto + (produto * 20 / 100)
    soma = produto / parcela
    print('sua compra sera parecelada em {}x de {:.2f} com juros'.format(parcela,soma))
    print('sua compra de {} vai custar R$ {} no final.'.format(produto,maisde3))

    
print('muito obrigado por comprar em nossa loja')


    
    
    

