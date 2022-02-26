a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a == b or a == c:
    if b == c:
        print('3')
    else:
        print('2')
else:
    if b == c:
        print('2')
    else:
        print('0')