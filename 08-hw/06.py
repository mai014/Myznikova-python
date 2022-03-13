str = input('Введите строку: ')
count = 0
number_list = []
for letter in str:
    if letter == 's':
        count += 1
    else:
        number_list.append(count)
        count = 0
n_max = max(number_list)
print('Зашифровано число:', n_max)