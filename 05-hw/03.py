n = int(input('Введите число: '))
i = 1
while n // 10 != 0:
    n /= 10
    i += 1
print(i, 'десятичных цифр.')