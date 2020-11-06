
valores = []
par = []
impar = []

while True:
    valores.append(int(input('digite um numero ? ')))
    resposta = str(input('quer continuar [N/s] ? '))
    if resposta in 'Nn':
        break

for indice , numero in enumerate(valores):
    
    if numero % 2 == 0:
        par.append(numero)

    if numero % 2 == 1:
        impar.append(numero)

print(f'quantos {len(valores)} elementos')
print(f'os numeros digitados foram {valores}')
print(f'os numeros pares são {par}')
print(f'os numero impar são {impar}')
        
