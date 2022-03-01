a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))
num = a
average = 0
i = 0
while num <= b:
    if num % 3 == 0:
        average += num
        if num != 0:
            i += 1
    num += 1
print(average)
print(i)
average /= i
print('Среднее арифметическое чисел, делящихся на 3 равно:', average)