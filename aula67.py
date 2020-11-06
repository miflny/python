def linha():
    print('=-' * 46)

linha()
linha()

time = ('palmeiras','são paulo','corinthias','santos','flamento')


linha()
print(f'tabela do brasileirão 2020 {time}')
linha()
print('os primeiros colocados são {}'.format(time[:2]))
linha()
print(f'os ultimos colocados da tabela {time[3:]}')
linha()
print(f'os times em ordem alfabetica {sorted(time)}')
linha()
print(f'o santos esta na {time.index("santos") +1}ª posição')
linha()
linha()

