from day2input import day2input

test_input = '''A Y
B X
C Z'''

rock = 1
paper = 2
scissor = 3

win = 6
draw = 3
lose = 0

rules = {
    'A X': rock + draw,  
    'A Y': paper + win,
    'A Z': scissor + lose,
    'B X': rock + lose,
    'B Y': paper + draw,
    'B Z': scissor + win,
    'C X': rock + win,
    'C Y': paper + lose,
    'C Z': scissor + draw,
}

rules_2 = {
    'A X': scissor + lose,  
    'A Y': rock + draw,
    'A Z': paper + win,
    'B X': rock + lose,
    'B Y': paper + draw,
    'B Z': scissor + win,
    'C X': paper + lose,
    'C Y': scissor + draw,
    'C Z': rock + win,
}

result = []
for game in test_input.splitlines():
    result.append(rules[game])

  
print(result)
print(sum(result))

result = []
for game in day2input.splitlines():
    result.append(rules[game])

print(sum(result))

result = []
for game in day2input.splitlines():
    result.append(rules_2[game])

print (sum(result))