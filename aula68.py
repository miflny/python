

times = ('palmeiras','são paulo','corinthias','santos','bahia','flamengo','vasco','gremio','inter','avai')

op = 0
while op != 5:
    print('======================================')
    print('=================MENU=================')
    print('''
    [1] tabela do brasileirão
    [2] 5 os primeiros colocados
    [3] os 2 ultimos colocados
    [4] ordem alfabetica
    [5] sair do programa
    ''')
    op = int(input('qual sua opção ?? '))
    
    if op == 1:
        print(times)
    elif op == 2:
        print(times[:5])
    elif op == 3:
        print(times[8:])
    elif op == 4:
        print(sorted(times))

