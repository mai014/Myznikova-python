text = input('Введите текст: ')
text_list = list(text)
vowel_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'я', 'ю', 'э', 'ы', 'А', 'Е', 'Ё', 'И', 'О', 'У', 'Я', 'Ю', 'Э', 'Ы']
new_list = [letter for letter in text_list if letter in vowel_list]
print('Список гласных букв:', new_list)
print('Длина списка:', len(new_list))
