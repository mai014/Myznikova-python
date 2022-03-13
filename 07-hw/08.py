n = int(input('Введите количество членов ряда: '))
s = 1
for i in range(1, n + 1):
    s += float((-1)**n/(2**n))
print('Сумма ряда равна', s)