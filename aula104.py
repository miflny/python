

ficha = [

]

while True:
    nome = str(input('nome : '))
    p1 = float(input(' Prova 1 : '))
    p2 = float(input('Prova 2 : '))
    media = (p1 + p2)/2
    ficha.append([nome,[p1,p2] ,media])
    resp = str(input('Quer continuar [N\S] : '))
    if resp in 'Nn':
        break
print(f'{"NO.":<4}{"NOME":<10}{"MEDIA":>8}')
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:8.1f}')
while True:
    pessoa = int(input('Mostrar nota de qual aluno (999 interrompe) : '))
    if pessoa == 999:
        break
    print(f'{ficha[pessoa] [0]} são {ficha[pessoa] [1]}')
    