n = 1
i = 0
while n != 0:
    n = int(input('Введите число: '))
    if n % 2 == 0:
        i += 1
i -= 1
print('Чётных чисел:', i)