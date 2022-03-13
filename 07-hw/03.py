time = int(input('Сколько минут до взрыва? '))
for i in range(time, -1, -1):
    ans = input('Хотите обезвредить бомбу? ')
    if ans == 'да':
        print('Бомба обезврежена за', time - i, 'мин.')
        break
else:
    print('Бомба взорвалась.')
    