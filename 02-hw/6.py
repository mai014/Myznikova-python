num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
a1 = num1 % 100
tens1 = a1 // 10
ones1 = a1 % 10
a2 = num2 % 100
tens2 = a2 // 10
ones2 = a2 % 10
total = tens1 * 10 + tens2 * 10 + ones1 + ones2
print('Сумма:', total)