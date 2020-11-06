


time = ('palmeiras','santos','flamengo','corinthias','são paulo','vasco','flamengo')

opcao = 0
while opcao != 5:
    print('''
    [1] times do brasileirao
    [2] 5 primeiros colocados
    [3] os 4 primeiro colocado
    [4] em que lugar o corinthias ta 
    [5] sair do programa
    ''')
    
    opcao = int(input('Qual opção vc esolhe ? '))

    if opcao == 1:
        print(time)
    elif opcao == 2:
        print(time[:4])
    elif opcao == 3:
        print(time[4:])
    