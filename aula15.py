


nome = str(input('qual é o seu nome ?? '))

if nome == 'miflny':
    print('       que nome lindo vc tem ')
elif nome == 'pedro'or nome == 'maria 'or nome == 'vitoria':
    print('seu nome é tão popular no brasil')
elif nome in 'ana,claudia, maria, melissa':
    print('que belo nome feminino')
else:
    print('seu nome é tão comum (:|')
print('tenha um boom dia {}'.format(nome))