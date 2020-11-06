
partida = [

]
jogador = {

}
jogador['nome'] = str(input('nome do jogador '))
tot = int(input(f'quantas partidas {jogador["nome"]} jogou '))
for contador in range(0,tot):
    partida.append(int(input(f'Quantos gols na partida {contador} : ')))
jogador['gols'] = partida [:]
jogador['total'] = sum (partida)
print(jogador)
print('='* 50)
for k , v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('='* 50)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i , b in enumerate(jogador["gols"]):
    print(f'    => na partida {i} fez {b} ')
print(f'foi um total de {jogador["total"]} gols.')
print('='*50)