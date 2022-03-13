num_list1 = []
num_list2 = []
print('Введите три числа в первый список: ')
for i in range(0, 3):
    num1 = int(input())
    num_list1.append(num1)
print('Введите семь чисел во второй список: ')
for j in range(0, 7):
    num2 = int(input())
    num_list2.append(num2)
print('Первый список:', num_list1)
print('Второй список:', num_list2)
num_list = num_list1 + num_list2
new_set = set(num_list)
new_list = list(new_set)
print('Новый первый список с уникальными элементами:', new_list)

