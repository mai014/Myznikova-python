str = input('Вводите строку из 10 символов (a-свободное стойло, b-занятое): ')
i = 0
total = 0
for symbol in str:
    i += 1
    milk = 2 ** i
    if symbol == 'b':
        total += milk
print('Всего молока будет', total, 'л.')