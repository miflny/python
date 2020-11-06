
idade = int(input('digite sua idade ?? '))

print(' A idade do atleta é {}'.format(idade))


if idade <= 9:
    print('ATLETA MIRIM')
elif idade >= 10 and idade <= 14:
    print('infantil')
elif idade >= 14 and idade < 19:
    print('JUNIOR')
elif idade >= 19 and idade <= 22:
    print('SENIOR')
else:
    print('MASTER')
