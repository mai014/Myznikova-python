total = int(input('Общая длина колонтитула: '))
middle = int(input('Желаемое количество восклицательных знаков: '))
wave = int((total - middle) / 2)
str = '~' * wave + '!' * middle + '~' * wave
print(str)