n_max = int(input('Введите максимальное число: '))
num_lst = [i for i in range(1, n_max + 1)]
new_lst = num_lst
lst = []
lst = input('Нужное число есть среди чисел: ')
while lst != 'Помогите!':
    lst_new = list(lst.split(' '))
    for i in range(0, len(lst_new)):
        lst_new[i] = int(lst_new[i])
    ans = input('Ответ Артёма: ')
    if ans == 'Нет':
        new_lst = [n for n in new_lst if n not in lst_new]
    elif ans == 'Да':
        new_lst = lst_new
    lst = input('Нужное число есть среди чисел: ')
print('Артём мог загадать следующие числа:', new_lst)