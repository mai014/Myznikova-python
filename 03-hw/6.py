points1 = int(input('Кубик Кости: '))
points2 = int(input('Кубик владельца: '))
if points1 > points2:
    print('Разность:', points1 - points2)
    print('Костя платит')
elif points1 == points2:
    print('Разность:', points1 - points2)
else:
    print('Сумма:', points1 + points2)
    print('Владелец платит')
print('Игра окончена')