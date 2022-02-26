n = int(input('Введите количество опыта: '))
level = 0
if n < 1000:
    level = 1
elif n < 2500:
    level = 2
elif n < 5000:
    level = 3
else:
    level = 4
print('Ваш уровень:', level)

