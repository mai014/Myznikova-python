n = int(input('Введите кол-во заказов: '))
d = dict()
for i in range(1, n + 1):
    print(i, 'заказ: ', end='')
    order = (input('')).split(' ')
    name = order[0]
    pizza = order[1]
    num = int(order[2])
    if name not in d:
        d[name] = {pizza: num}
    else:
        if pizza not in d[name]:
            d[name][pizza] = num
        else:
            d[name][pizza] += num
print(d)
for fam, elem in sorted(d.items()):
    print(fam, ':')
    for name_pizza in elem.keys():
        print('  ', name_pizza, ':', elem[name_pizza])

