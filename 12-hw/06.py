n = int(input('Введите кол-во пар слов: '))
syn_d = dict()
for i in range(1, n + 1):
    print(i, 'пара: ', end='')
    word_list = (input('')).lower().split('-')
    syn_d[word_list[0]] = word_list[1]
word = input('Введите слово: ').lower()
if word in syn_d == False:
    word = input('Введите слово: ').lower()
else:
    for key, value in syn_d.items():
        if word == key:
            print('Синоним:', value)
        elif word == value:
            print('Синоним:', key)
