

ficha = [

]
while True:
    nome = str(input('nome : '))
    n1 = float(input('nota 1 : '))
    n2 = float(input('nota 2 : '))
    media = (n1 + n2) /2
    ficha.append([nome , [n1 , n2] ,media ])
    resp = str(input('Quer continuar [N\S] : '))
    if resp in 'Nn':
        break
print('-'*35)
print(f'{"NO.":<4}{"NOME":<10}{"media":>8}')
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4} {aluno[0]:<10}{aluno[2]:>8.1f}')
print('-'*35)
while True:
    pessoa = int(input('Mostrar a nota de qual aluno (999 interrompe) : '))
    if pessoa == 999:
        break
    if pessoa <= len(ficha):
        print(f'Nota do aluno {ficha[pessoa] [0].upper()} são {ficha[pessoa] [1]}')