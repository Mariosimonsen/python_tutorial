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
        num1, num2, = [int(num) for num in equation.split('+')]
        op = operators['+']
    elif '-' in equation:
        num1, num2 = [int(num) for num in equation.split('-')]
        op = operators['-']
    elif '**' in equation:
        num1, num2 = [int(num) for num in equation.split('**')]
        op = operators['**']
    elif '*' in equation:
        num1, num2 = [int(num) for num in equation.split('*')]
        op = operators['*']
    elif '/' in equation:
        num1, num2 = [int(num) for num in equation.split('/')]
        op = operators['/']
    elif '%' in equation:
        num1, num2 = [int(num) for num in equation.split('%')]
        op = operators['%']
    return op(num1, num2)
   
print(calculation(str(calculation('2+2')) + '+ 2')) # forklar til Eivind hvorfor dette fungerer
