v = int(input('Скорость Васи в км/ч: '))
t = int(input('Время поездки в часах: '))
s = v * t
point = s % 115
print('Вася остановится на', point, '-ом километре')