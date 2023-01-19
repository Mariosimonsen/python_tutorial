from day3input import day3_input
from string import ascii_letters


test_input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

result = []

for line in test_input.splitlines():
    mid = len(line)//2
    left = line[:mid]
    right = line[mid:]
    intersection = set(left).intersection(set(right))
    char = intersection.pop()
    result.append(ascii_letters.index(char) + 1)

print (sum(result))

result = []

for line in day3_input.splitlines():
    mid = len(line)//2
    left = line[:mid]
    right = line[mid:]
    intersection = set(left).intersection(set(right))
    char = intersection.pop()
    result.append(ascii_letters.index(char) + 1)

print (sum(result))

party = day3_input.splitlines()
groups = []

for i in range(0, len(party), 3):
    group = party[i], party[i+1], party[i+2]
    groups.append(group)
    line1 = party[i]
    line2 = party[i+1]
    line3 = party[i+2]
    intersection = set(line1).intersection(set(line2)).intersection(set(line3))
    value = intersection.pop()
    groups.append(ascii_letters.index(value) + 1)

for i in range(0, len(party), 3):
    line1 = party[i]
    line2 = party[i+1]
    line3 = party[i+2]
    intersection = set(line1).intersection(set(line2)).intersection(set(line3))
    value = intersection.pop()
    groups.append(ascii_letters.index(value) + 1)

print(sum(groups))



    
