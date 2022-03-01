i = 1
average = 0
while i <= 12:
    print('Введите зараплату за', i, '-й мeсяц: ', end="")
    salary = int(input())
    average += salary
    i += 1
average = int(average / 12)
print('Средняя зарплата равна:', average)