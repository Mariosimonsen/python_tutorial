from day4_input import day4_input
import re 
test_input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

a, b, c, d = 2, 6, 4, 8
print(a <= c and d <= b or c <= a and b <= d)

result = []

for line in day4_input.splitlines():
    a, b, c, d = [int(num) for num  in re.findall('[0-9]+', line)]
    result.append(a <= c and d <= b or c <= a and b <= d)

print (sum(result))

result = []

for line in day4_input.splitlines():
    elf1, elf2 = line.split(',')
    a, b = elf1.split('-')
    c, d = elf2.split('-') 
    a, b, c, d = int(a), int(b), int(c), int(d)
    result.append(a <= c <= b or b <= d <= a or c <= a <= d or b <= d <= a)
   

print (sum(result)) 

'''
.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
'''