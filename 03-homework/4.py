price1 = int(input('Цена первого стула: '))
price2 = int(input('Цена второго стула: '))
price3 = int(input('Цена третьего стула: '))
total = price1 + price2 + price3
if total > 10000:
    total *= 0.1
print('Итог:', total)