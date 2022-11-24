from calculator import operators

main_operators = ('+', '-', '*', '/', '%', '**')
'''
def calculation(equation):
    if '+' in equation:
        y = equation.split('+')
        x = int(y[0]) + int(y[1])


    elif '-' in equation:
        y = equation.split('-')
        x = int(y[0])-int(y[1])
    return x 


calculation('2+3')

'''

def calculation(equation):
    if '+' in equation:
        num1, num2, = [float(num) for num in equation.split('+')]
        op = operators['+']
    elif '-' in equation:
        num1, num2 = [float(num) for num in equation.split('-')]
        op = operators['-']
    elif '**' in equation:
        num1, num2 = [float(num) for num in equation.split('**')]
        op = operators['**']
    elif '*' in equation:
        num1, num2 = [float(num) for num in equation.split('*')]
        op = operators['*']
    elif '/' in equation:
        num1, num2 = [float(num) for num in equation.split('/')]
        op = operators['/']
    elif '%' in equation:
        num1, num2 = [float(num) for num in equation.split('%')]
        op = operators['%']
    return op(num1, num2)
   
print(calculation(str(calculation('2+2')) + '+ 2')) # forklar til Eivind hvorfor dette fungerer

# Divide and conquer
'2 + 2'
verdi = calculation('2 + 2')

'4 + 2 + 3 - 7 / 3'
part1 = calculation('4 + 2')
part2 = calculation(f'{part1} + 3')
part3 = calculation(f'{part2} - 7')
part4 = calculation(f'{part3} / 3')

total = calculation(str(calculation('4 + 2') + ' + 3'))

#Etter beste evene lage en kortstokk, la det være strings, kan lagres i en liste, mulighet og skrive alle verdiene i en listen 2s,3s osv
rank, suit = '2345678910jqka', 'h'