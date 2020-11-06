
distancia = float(input('diga a sua distancia ?? '))

print('vc esta preste a ter uma viagem de {}'.format(distancia))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('R$ {:.2f}'.format(preco))
