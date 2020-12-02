import requests
def main():


    print('######################')
    print('#### Consulta Cep ####')
    print('######################')
    print()

    cep = input('digite um cep : ')
    print()

    if len(cep) !=8:
        print('quantidade de digito invalido')
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    data = request.json()
    if 'erro' not in data:
        print(f'cep : {data["cep"]}')
        print(f'rua : {data["logradouro"]}')
        print(f'bairro : {data["bairro"]}')
        print(f'cidade : {data["localidade"]}')
        print(f'uf : {data["uf"]}')

    opcao = int(input('quer continuar\n[1]sim\n[2]nao\n'))
    if opcao == 1:
        main()
if __name__ == '__main__':
    main()
else:
    print('cef errado')