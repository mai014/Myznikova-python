point1 = int(input('Введите количество баллов по русскому языку:'))
point2 = int(input('Введите количество баллов по математике:'))
point3 = int(input('Введите количество баллов по информатике:'))
point = point1 + point2 + point3
if point >= 270:
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошёл на бюджет!')