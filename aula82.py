
palavras = ('miflny', 'aprender','programar','estudar','programador','mercador','melancia',
            'gratis','lapis','mochila','python','praticar','curso','futuro',)

for indice in palavras:
    print(f'\nNa palavra {indice.upper()} tenho',end=' ')
    
    for letra in indice:
        if letra in 'aeiou':
            print(f'{letra.lower()}',end='')
        

    