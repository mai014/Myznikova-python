num = int(input('Введите число: '))
thousands = num // 1000
a = num % 1000
hundreds = a // 100
b = a % 100
tens = b // 10
ones = b % 10
print(thousands, hundreds, tens, ones)