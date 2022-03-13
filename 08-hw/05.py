x = 8
y = 10
while True:
    print('Робот находиться в точке (', x, ',', y, ')', sep='')
    command = input('В какую сторону хотите направить робота(север(W), юг(S), запад(A), восток(D)): ')
    if command == 'W':
        if y < 20:
            y += 1
        else:
            print('Измените маршрут!')
    elif command == 'S':
        if y > 0:
            y -= 1
        else:
            print('Измените маршрут!')
    elif command == 'A':
        if x > 0:
            x -= 1
        else:
            print('Измените маршрут!')
    elif command == 'D':
        if x < 15:
            x += 1
        else:
            print('Измените маршрут!')
