print('Введите десять чисел через Enter: ')
i = 0
j = 1
while j <= 10:
    n = int(input())
    if n % 2 == 0 and n > 0:
        i += 1
    j += 1
print('Кол-во четных положительных чисел:', i)
