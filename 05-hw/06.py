n = 1
pos = 0
neg = 0
while n != 0:
    n = int(input('Введите число: '))
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
print('Количество положительных чисел:', pos)
print('Количество отрицательных чисел:', neg)