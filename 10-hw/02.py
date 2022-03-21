N = int(input('Введите длину списка: '))
new_list = [1 if n % 2 == 0 else n % 5 for n in range(0, N)]
print('Результат:', new_list)