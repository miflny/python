
jogador = {

}
partida = []
jogador['nome'] = str(input('nome do jogador : '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou : '))
for contador in range(0,tot):
    partida.append(int(input(f'Quantos gols na partida {contador} ? ')))
print('=' * 50)
jogador['gols'] = partida [:]
jogador['total'] = sum (partida)
print(jogador)
print('=' * 50)
for k , v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('='* 50)
print(f' O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i , v in enumerate(jogador["gols"]):
    print(f'    => na partida {i} , fes {v} gols.')
print('=' * 50)