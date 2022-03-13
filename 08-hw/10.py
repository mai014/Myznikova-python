code = input('Введите зашифрованное сообщение: ')
n = len(code)
word_list = []
count = int(n / 2)
num = 0
if n % 2 == 0:
    for i in range(0, count):
        word_list.insert(i, code[2 * i])
    for j in range(count, n):
        word_list.insert(j, code[n - (2 * num + 1)])
        num += 1
else:
    for i in range(0, count + 1):
        word_list.insert(i, code[2 * i])
    for j in range(count + 1, n):
        word_list.insert(j, code[n - 1 - (2 * num + 1)])
        num += 1
print('Расшифрованное слово: ', end='')
print(''.join(word_list))