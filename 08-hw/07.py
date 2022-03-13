str = input('Введите слова через пробел: ')
str += ' '
number_list = []
count = 0
for sign in str:
    if sign != ' ':
        count += 1
    else:
        number_list.append(count)
        count = 0
max_num = max(number_list)
print('Самое длинное слово состоит из', max_num, 'букв')