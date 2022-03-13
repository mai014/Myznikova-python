message = input('Введите сообщение: ')
i = 1
for symbol in message:
    if symbol != '*':
        i += 1
    else:
        break
print('Символ * стоит на', i, 'месте')

