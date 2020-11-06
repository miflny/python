s = 0
opcao = 5
while opcao != 5:
    m = int(input('digite um numero '))
    o = int(input('digite outro numero '))
    
    print('''
    [1] somar
    [2] multiplicar''')
    
    if opcao == 1:
        s = m + o
        print(s)
    elif opcao == 2:
        s = m * o
    print(s)
   

