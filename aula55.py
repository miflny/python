

par = 0
impar = 0 
v = 1
while v != 0:
    v = int(input('soma de numeros IMPAR e PAR  '))
    if v != 0:
        if v % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('voce digitou {} é numeros pares {} é impar'.format(par, impar))
print('FIM')
