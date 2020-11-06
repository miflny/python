
soma = 0
m = int(input('digite um numero '))
o = int(input('digite outro numero '))

opcao = 0
while opcao != 5:
    print('===========MENU===========')
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5]sair do programa
    ''')
    print('==========================')

    opcao = int(input('qual sua opção ?? '))

    if opcao == 1:
        soma = m + o
        print(soma)
       
    elif opcao == 2:
        soma = m * o
        print(soma)
    elif opcao == 3:
       if m > o:
        print(m)
       elif m == o:
        print(m,o)
       else:
            print(o)
    elif opcao == 4:
        m = int(input('digite um numero ?? '))
        o = int(input('digite outro numero ?? '))
    else:
        print()




   
        
    
 
