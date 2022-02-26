a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a < b:
    if b < c:
        print('Максимум равен', c)
    else:
        print('Максимум равен', b)
else:
    if a < c:
        print('Максимум равен', c)
    else:
        print('Максимум равен', a)