
conte = ('zero','um','dois','tres','quatro','cinco')

while True:

    num = int(input('digite um numero entre 0 a 5 : '))
    
    if num >= 0 and num <= 5 :
        break
    print('tente novamente')
print(f'vc digitou o numero {conte[num]}')
