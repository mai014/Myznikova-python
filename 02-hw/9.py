num = int(input('Введите число: '))
thousands = num // 1000
a = num % 1000
hundreds = a // 100
b = a % 100
tens = b // 10
ones = b % 10
new_num = ones * 1000 + tens * 100 + hundreds * 10 + thousands
print('Обратное число:', new_num)