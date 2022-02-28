credit = int(input('Введите сумму долга: '))
name = input('Введите ваше имя: ')
print(name + ', ваша задолженность составляет', credit, 'рублей.')
fee = int(input('Сколько рублей вы внесёте? '))
while fee < credit:
    print('Маловато', name + '.Давайте ещё раз')
    fee = int(input('Сколько рублей вы внесёте? '))
print('Отлично,', name + '! Вы погасили долг.')