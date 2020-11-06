

n3 = float(input('digite a nota ?? '))
n4 = float(input('digite a segunda nota ?? '))

nota = (n3 +n4) /2
print('tirando {:.1f} e {:.1f}, é a media do aluno é {:.1f}'.format(n3,n4,nota))
if nota < 5.0:
    print('REPROVADO')
elif nota > 5.0  and nota < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
