from day1_input import day1_input

test_calories = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

def solution_one(calories):
    total = 0
    my_answers = []
    for line in calories.splitlines():
        if line == '':
            my_answers.append(total)
            total = 0
        else:
            total = total + int(line)

    my_answers.sort()
    return my_answers[-1] 
    
print(solution_one(day1_input))


def solution_two(calories):
    total = 0
    my_answers = []
    for line in calories.splitlines():
        if line == '':
            my_answers.append(total)
            total = 0
        else:
            total = total + int(line)

    my_answers.sort()
    return my_answers[-3:] 
    

print(sum(solution_two(day1_input)))

