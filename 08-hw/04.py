rows = int(input('Введите кол-во рядов: '))
seats = int(input('Введите кол-во сидений в ряду: '))
distance = int(input('Введите кол-во метров между рядами: '))
str1 = ''
for n1 in range(0, seats):
    str1 += '='
for n2 in range(0, distance):
    str1 += '*'
for n1 in range(0, seats):
    str1 += '='
str1 += '\n'
str = str1 * rows
print(str)