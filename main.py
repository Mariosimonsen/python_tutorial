from calculator import add, sub, mul, truediv, truediv

valid_operators = ('add', 'sub', 'multi', 'truediv', 'div')

while True:
    operator = input(f'Hva vil du gjøre?\n{valid_operators}\ner dine valg: ')
    operator = operator.lower()
    if operator in valid_operators:
        break
    else:
        print('du valgte ikke en gyldig operator, prøv igjen!\n')


math_operators = (add, sub, mul, truediv, truediv)

#'add' er i index 0

index_of_operator = valid_operators.index(operator)

while True:
    num_1 = input('Skriv inn det første tallet: ')
    if not num_1.isdecimal():
        print('ugyldig tall, prøv igjen\n\n')
        continue
    else:
        num_1 = int(num_1)
        break

# lage en while loop for num_2

while True:
    num_2 = input('Skriv inn det andre tallet: ')
    if not num_2.isdecimal():
        print('Ugyldig tall, prøv igjen')
        continue
    else:
        num_2 = int(num_2)
        break
    
my_operator = math_operators[index_of_operator]
print(my_operator(num_1, num_2))

