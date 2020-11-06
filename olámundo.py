n1 = float(input("digite um numero "))

n2 = float(input("digite outro numero "))

print("""
[1]soma\n
[2]subitracao\n
[3] multiplicacao\n
[4]divisao

""")
opcao = int(input("qual o peracao vc quer "))

if opcao == 1:
    print(n1 + n2)
elif opcao == 2:
    print(n1 - n2)
elif opcao == 3:
    print(n1 * n2)
elif opcao == 4:
    print(n1 / n2)

    def escrever_json(dados):
    with open('meu_arquivo.json', 'w', encoding='utf8')as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(','':'))
meu_dict = {
    'Titulo': 'Title',
    'Ano': 'Year',
    'Duração':'Runtime',
    'Genero': 'Genre',
    'Diretor': 'Director',
    'Atores': 'Actors'


}
if opcao == 1:
    print(w)

escrever_json(meu_dict)



int(input('Cadastrar, digite 1\nConsultar, digite 2 \nOpção: '))
 print() if opc == 1:  
    banco = (NovaConta()) 
        lista.append(banco) 
            print('Cadastrado com sucesso! \nID: %i \nCliente: %s \nConta: %i '        
               %(banco.ID, banco.cliente, banco.conta))   
                 print('-'*25) elif opc == 2: 
                      consulta = int(input('Digite o ID: '))   
                        if consulta not in lista:        
                             print('Não contém')  
                                else:         print(consulta[lista])**
    

