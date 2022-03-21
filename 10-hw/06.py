N = int(input('Введите число элементов списка: '))
num_list = []
for i in range(0, N):
    num = int(input('Введите число: '))
    num_list.append(num)
new_list = [elem for elem in num_list if elem != 0]
print('Новый список без нулей:', new_list)
