s = int(input('Введите пробег: '))
num = int(input('Введите сегодняшнее число: '))
hundreds = s // 100
s1 = s % 100
tens = s1 // 10
ones = s1 % 10
total = hundreds + tens + ones
if total > num:
    print('Сброс.')
    print('Пробег: 0')
else:
    print('Сегодня не сломался.')
    print('Пробег:', s)