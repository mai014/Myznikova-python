n = int(input('Введите число: '))
m = n
factorial = 1
if n == 0:
    factorial = 1
else:
    while n >= 1:
        factorial *= n
        n -= 1
print('Факториал числа', m, 'равен:', factorial)
