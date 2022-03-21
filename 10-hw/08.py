N = int(input('Кол-во палок: '))
game_list = []
for _ in range(0, N):
    game_list.append('|')
K = int(input('Кол-во бросков: '))
for i in range(1, K + 1):
    print('Бросок', i, '. Сбиты палки с номера', end=' ')
    start = int(input())
    print('по номер ', end='')
    end = int(input())
    for j in range(start - 1, end):
        game_list[j] = '.'
print('Результат: ', ''.join(game_list))