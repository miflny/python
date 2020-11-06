

jogador = {

}
partida = [

]
while True:
    jogador['nome'] = str(input('Nome do Jogador : '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogoou ? '))

    for contador in range(0,tot):
        partida.append(int(input(f'Quantos gols na partida {contador} ? ')))
    jogador['gols'] = partida [:]
    jogador['total'] = sum (partida)
    resposta = str(input('Quer continuar [N/S] ? '))
    if resposta in 'Nn':
        break
print('=' * 50)
print(f'{"cod nome":<4}{"gols":>8}{"total":>10}')
for k , v in jogador.items():
    print(jogador,end='')
    print()
    pessoa = int(input('Mostrar dados de qual jogador (999 interompe) ? '))
    if pessoa == 999:
        break
    if pessoa <= len(jogador):
        print('-' * 50)
    print(f'--LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
    for x , y in enumerate(jogador['gols']):
        print(f'   => No jogo {x}, fez {y} gols.')
    print('=' * 50)

