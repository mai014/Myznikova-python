number = int(input('Загадали число: '))
attempt = int(input('Введите число: '))
i = 1
while number != attempt:
    if attempt > number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
        attempt = int(input('Введите число: '))
        i += 1
    elif attempt < number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
        attempt = int(input('Введите число: '))
        i += 1
print('Вы угадали! Число попыток:', i)
