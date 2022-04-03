text = list(input('Введите текст: '))
init_d = dict()
freq = 0
for i in range(0, len(text)):
    for letter in text:
        if text[i] == letter:
            freq += 1
    init_d[text[i]] = freq
    freq = 0
new_d = dict()
letter_list = []
for i in range(1, max(init_d.values()) + 1):
    for key, value in init_d.items():
        if value == i:
            letter_list.append(key)
    new_d[i] = letter_list
    letter_list = []
for num, list_letter in new_d.items():
    print(num, ':', list_letter)
