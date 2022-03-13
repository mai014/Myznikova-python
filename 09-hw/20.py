n = int(input('Кол-во чисел: '))
num_list = []
for i in range(1, n + 1):
    print(i, 'число: ', end='')
    num = int(input())
    num_list.append(num)
new_list = []
change_list = num_list
reverse_list = []
for elem in num_list:
    while reverse_list != change_list:
        new_list.insert(0, elem)
        change_list += new_list
        reverse_list = list(reversed(change_list))
print('Симметричный лист:', ' '.join(str(num) for num in change_list))


