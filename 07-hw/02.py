n = int(input('Введите количество должников: '))
sum = 0
for i in range(0, n, 5):
    print('Должник с номером', i)
    credit = int(input('Введите сумму вашего долга: '))
    sum += credit
print('Общая сумма долга:', sum)