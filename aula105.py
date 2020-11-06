
estado = {

}
brasil = [

]
for contador in range(0,3):
    estado['uf'] = str(input('unidade faderativa : '))
    estado['sigla'] = str(input('sigla do estado : '))
    brasil.append(estado.copy())
for est in brasil:
    for chave,valor in est.items():
        print(f'O campo {chave} tem valor {valor}')