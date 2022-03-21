letter_list = [' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
               'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
text = input('Введите сообщение: ')
index_list = [letter_list.index(text[i]) for i in range(0, len(text))]
h = int(input('Введите сдвиг: '))
for i in range(1, h + 1):
    letter_list.append(letter_list[i])
code_list = [letter_list[i+h] if i != 0 else ' ' for i in index_list]
print('Зашифрованное слово: ', end='')
for i in range(0, len(code_list)):
    print(code_list[i], end='')