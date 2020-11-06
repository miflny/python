

jogador = {

}
partida =[

]
while True:
    jogador['nome'] = str(input('nome do jogador : '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    for contador in range(0,tot):
        partida.append(int(input(f'Quantos gols na partida {contador} ? ')))
    resp = str(input('Quer continuar [N/S] ? '))
    print('-'*50)
    if resp in 'Nn':
        break
print('-' * 50)
print(f'{"cod nome":<4}{"gols":>8}{"total":>10}')
print('-' * 50)


while True:
    pessoa = int(input(f'Mostrar dados de qual jogador (999 interompe) ? '))
    if pessoa == 999:
        break
    print(f'--LEVATAMENTO DO JOGADOR {jogador["nome"]}:')


