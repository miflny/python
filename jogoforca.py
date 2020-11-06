palavra_secreta = ["B","A","N","A","N","A"]
letras_descobertas = []


print('-='* 20)
print('Bem vindo ao jogo da forca')
print('-='* 20)
print('-----------------------------')
print('A forca é uma fruta')
print('-----------------------------')



for i in range(0, len(palavra_secreta)): 
    letras_descobertas.append("-")
acertou = False
while acertou == False:

    letra = str(input('digite uma letra ?? ')).upper()
    for i in range(0, len(palavra_secreta)): 
        if letra == palavra_secreta[i]:
           letras_descobertas[i] = letra
        print(letras_descobertas[i])
    acertou = True
    for x in range(0, len(letras_descobertas)):
        if letras_descobertas [x] == "-":
           acertou = False
print('Fim Jogo')