five, four, three = 0, 0, 0
entered_list = input('Введите список оценок: ').split()
point = list(map(int, entered_list))
for num in point:
    if num == 5:
        five += 1
    elif num == 4:
        four += 1
    else:
        three += 1
if five < four:
    if four < three:
        print('Сегодня больше троечников.')
    else:
        print('Сегодня больше хорошистов.')
else:
    if five < three:
        print('Сегодня больше троечников.')
    else:
        print('Сегодня больше отличников.')