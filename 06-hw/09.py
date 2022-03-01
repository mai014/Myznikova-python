entered_list = input('Введите десять чисел: ').split()
num_list = list(map(int, entered_list))
count = 1
for i in range (len(num_list) - 1):
    if num_list[i+1] > num_list[i]:
        count += 1
if count == 10:
    print('Числа упорядочены по возрастанию.')
else:
    print('Числа не упорядочены по возрастанию.')