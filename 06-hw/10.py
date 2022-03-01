N = int(input('Введите число карточек: '))
print('Последовательно введите', N - 1, 'оставшихся карточек: ')
entered_list = input().split()
num_list = list(map(int, entered_list))
count = 0
for i in range(1, N):
    for num in num_list:
        if i != num:
            count += 1
    if count == N - 1:
        miss = i
print(miss)