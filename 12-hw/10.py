text = list(input('Введите строку: '))
d = dict()
count = 0
odd = 0
for i in range(len(text)):
    if text[i] in d:
        d[text[i]] += 1
    else:
        d[text[i]] = 1
if len(text) % 2 == 0:
    for num in d.values():
        if num % 2 == 0:
            count += 1
    if count == len(d):
        print('Можно сделать палиндром.')
    else:
        print('Нельзя сделать палиндром.')
else:
    for num in d.values():
        if num % 2 != 0:
            odd += 1
    if odd == 1:
        print('Можно сделать палиндром.')
    else:
        print('Нельзя сделать палиндром.')