deposit = int(input('Сумма вклада в банке: '))
percent = int(input('На сколько увиличится вклад: '))
result = int(input('В конце ваш вклад составит: '))
years = 0
while deposit < result:
    deposit = int(deposit + percent * deposit / 100)
    years += 1
print(years)
