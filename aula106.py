
aluno = {}

aluno ['nome'] = str(input(' Nome : '))
aluno ['media'] = float(input(f'media de {aluno["nome"]} : '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperaçao'
else:
    aluno['situação'] = 'Reprovado'
for chave, valor in aluno.items():
    print(f'{chave} {valor}')



