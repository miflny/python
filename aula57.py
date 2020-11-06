
s = 0
v = int(input('digite um valor '))
x = int(input('digite outro valor '))

print('================MENU================')
print('''
[1] somar
[2] mult
[3] mair 
[4] novos 
[5] sair''')
print('===================================')

op = int(input('Escolha um opção ?? '))
op = 0

while op != 5:

    if op == 1:
        s = v + x
        print(s)
        