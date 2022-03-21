text = input('Введите строку, содержащую, как минимум, две буквы h: ')
h_list = [i for i in range(0, len(text)) if text[i] == 'h']
first = min(h_list)
end = max(h_list)
print('Новая строка:', text[first: end + 1])