n = int(input('Введите свой доход: '))
if n > 50000:
    s = 0.3 * (n - 50000) + 0.2 * 40000 + 0.13 * 10000
elif n > 10000:
    s = 0.2 * (n - 10000) + 0.13 * 10000
else:
    s = 0.13 * n
print('Сумма налога:', s)