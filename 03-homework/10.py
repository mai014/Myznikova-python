num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
if num1 > num2:
    max1 = num1
else:
    max1 = num2
if num3 > max1:
    max2 = num3
else:
    max2 = max1
print('Максимальное число:', max2)